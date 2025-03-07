package provider

import (
	"context"
	"fmt"
	"strconv"

	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// Deployment controlling struct
type Deployment struct{}

// DeploymentArgs is defining what arguments it accepts
type DeploymentArgs struct {
	NodeID           interface{} `pulumi:"node_id"`
	Name             string      `pulumi:"name"`
	NetworkName      string      `pulumi:"network_name,optional"`
	SolutionType     string      `pulumi:"solution_type,optional"`
	SolutionProvider int64       `pulumi:"solution_provider,optional"`
	Disks            []Disk      `pulumi:"disks,optional"`
	ZdbsInputs       []ZDBInput  `pulumi:"zdbs,optional"`
	VmsInputs        []VMInput   `pulumi:"vms,optional"`
	QSFSInputs       []QSFSInput `pulumi:"qsfs,optional"`
}

// DeploymentState is describing the fields that exist on the created resource
type DeploymentState struct {
	DeploymentArgs

	NodeDeploymentID map[string]int64 `pulumi:"node_deployment_id"`
	ContractID       int64            `pulumi:"contract_id"`
	IPrange          string           `pulumi:"ip_range"`
	ZdbsComputed     []ZDBComputed    `pulumi:"zdbs_computed"`
	VmsComputed      []VMComputed     `pulumi:"vms_computed"`
	QsfsComputed     []QSFSComputed   `pulumi:"qsfs_computed"`
}

// Check validates the Deployment
func (*Deployment) Check(
	ctx context.Context,
	name string, oldInputs,
	newInputs resource.PropertyMap,
) (DeploymentArgs, []p.CheckFailure, error) {
	args, checkFailures, err := infer.DefaultCheck[DeploymentArgs](ctx, newInputs)
	if err != nil {
		return args, checkFailures, err
	}

	// TODO: bypass validation of empty node (will be assigned from scheduler)
	if nodeID, ok := args.NodeID.(string); ok && len(nodeID) == 0 {
		args.NodeID = 1
	}

	for i := range args.VmsInputs {
		if nodeID, ok := args.VmsInputs[i].NodeID.(string); ok && len(nodeID) == 0 {
			args.VmsInputs[i].NodeID = 1
		}
	}

	deployment, err := parseInputToDeployment(args, false)
	if err != nil {
		return args, checkFailures, err
	}

	return args, checkFailures, deployment.Validate()
}

// Create creates a deployment
func (*Deployment) Create(
	ctx context.Context,
	id string,
	input DeploymentArgs,
	preview bool) (string, DeploymentState, error) {
	state := DeploymentState{DeploymentArgs: input}
	if preview {
		return id, state, nil
	}

	config := infer.GetConfig[Config](ctx)

	nodeID, err := strconv.Atoi(fmt.Sprint(input.NodeID))
	if err != nil {
		return id, state, err
	}

	isLight, err := isZosLight(ctx, uint32(nodeID), config.TFPluginClient.NcPool, config.TFPluginClient.SubstrateConn)
	if err != nil {
		return id, state, err
	}

	deployment, err := parseInputToDeployment(input, isLight)
	if err != nil {
		return id, state, err
	}

	if err := config.TFPluginClient.DeploymentDeployer.Deploy(ctx, &deployment); err != nil {
		return id, state, err
	}

	if err := config.TFPluginClient.DeploymentDeployer.Sync(ctx, &deployment); err != nil {
		return id, state, err
	}

	state = parseDeploymentToState(deployment)

	return id, state, nil
}

// Update updates the arguments of the deployment resource
func (*Deployment) Update(
	ctx context.Context,
	id string,
	oldState DeploymentState,
	input DeploymentArgs,
	preview bool) (DeploymentState, error) {
	state := DeploymentState{DeploymentArgs: input}
	if preview {
		return state, nil
	}

	config := infer.GetConfig[Config](ctx)

	nodeID, err := strconv.Atoi(fmt.Sprint(input.NodeID))
	if err != nil {
		return state, err
	}

	isLight, err := isZosLight(ctx, uint32(nodeID), config.TFPluginClient.NcPool, config.TFPluginClient.SubstrateConn)
	if err != nil {
		return state, err
	}

	deployment, err := parseInputToDeployment(input, isLight)
	if err != nil {
		return state, err
	}

	if err := updateDeploymentFromState(&deployment, oldState, isLight); err != nil {
		return state, err
	}

	dl_network := config.TFPluginClient.State.Networks.GetNetwork(deployment.NetworkName)
	dl_network.SetNodeSubnet(deployment.NodeID, deployment.IPrange)

	if err := config.TFPluginClient.DeploymentDeployer.Deploy(ctx, &deployment); err != nil {
		return state, err
	}

	if err := config.TFPluginClient.DeploymentDeployer.Sync(ctx, &deployment); err != nil {
		return state, err
	}

	state = parseDeploymentToState(deployment)

	return state, nil
}

// Read gets the state of the deployment resource
func (*Deployment) Read(ctx context.Context, id string, oldState DeploymentState) (string, DeploymentState, error) {
	config := infer.GetConfig[Config](ctx)

	nodeID, err := strconv.Atoi(fmt.Sprint(oldState.DeploymentArgs.NodeID))
	if err != nil {
		return id, oldState, err
	}

	isLight, err := isZosLight(ctx, uint32(nodeID), config.TFPluginClient.NcPool, config.TFPluginClient.SubstrateConn)
	if err != nil {
		return id, oldState, err
	}

	deployment, err := parseInputToDeployment(oldState.DeploymentArgs, isLight)
	if err != nil {
		return id, oldState, err
	}

	if err := updateDeploymentFromState(&deployment, oldState, isLight); err != nil {
		return id, oldState, err
	}

	if err := config.TFPluginClient.DeploymentDeployer.Sync(ctx, &deployment); err != nil {
		return id, oldState, err
	}

	state := parseDeploymentToState(deployment)

	return id, state, nil
}

// Delete deletes a deployment resource
func (*Deployment) Delete(ctx context.Context, id string, oldState DeploymentState) error {
	config := infer.GetConfig[Config](ctx)

	nodeID, err := strconv.Atoi(fmt.Sprint(oldState.DeploymentArgs.NodeID))
	if err != nil {
		return err
	}

	isLight, err := isZosLight(ctx, uint32(nodeID), config.TFPluginClient.NcPool, config.TFPluginClient.SubstrateConn)
	if err != nil {
		return err
	}

	deployment, err := parseInputToDeployment(oldState.DeploymentArgs, isLight)
	if err != nil {
		return err
	}

	if err := updateDeploymentFromState(&deployment, oldState, isLight); err != nil {
		return err
	}

	if err := config.TFPluginClient.DeploymentDeployer.Cancel(ctx, &deployment); err != nil {
		return err
	}

	return nil
}
