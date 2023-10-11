// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package provider

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"internal"
)

type Deployment struct {
	pulumi.CustomResourceState

	Contract_id        pulumi.IntOutput        `pulumi:"contract_id"`
	Disks              DiskArrayOutput         `pulumi:"disks"`
	Ip_range           pulumi.StringOutput     `pulumi:"ip_range"`
	Name               pulumi.StringOutput     `pulumi:"name"`
	Network_name       pulumi.StringPtrOutput  `pulumi:"network_name"`
	Node_deployment_id pulumi.IntMapOutput     `pulumi:"node_deployment_id"`
	Node_id            pulumi.AnyOutput        `pulumi:"node_id"`
	Qsfs               QSFSInputArrayOutput    `pulumi:"qsfs"`
	Qsfs_computed      QSFSComputedArrayOutput `pulumi:"qsfs_computed"`
	Solution_provider  pulumi.IntPtrOutput     `pulumi:"solution_provider"`
	Solution_type      pulumi.StringPtrOutput  `pulumi:"solution_type"`
	Vms                VMInputArrayOutput      `pulumi:"vms"`
	Vms_computed       VMComputedArrayOutput   `pulumi:"vms_computed"`
	Zdbs               ZDBInputArrayOutput     `pulumi:"zdbs"`
	Zdbs_computed      ZDBComputedArrayOutput  `pulumi:"zdbs_computed"`
}

// NewDeployment registers a new resource with the given unique name, arguments, and options.
func NewDeployment(ctx *pulumi.Context,
	name string, args *DeploymentArgs, opts ...pulumi.ResourceOption) (*Deployment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Node_id == nil {
		return nil, errors.New("invalid value for required argument 'Node_id'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Deployment
	err := ctx.RegisterResource("grid:provider:Deployment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeployment gets an existing Deployment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeployment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentState, opts ...pulumi.ResourceOption) (*Deployment, error) {
	var resource Deployment
	err := ctx.ReadResource("grid:provider:Deployment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Deployment resources.
type deploymentState struct {
}

type DeploymentState struct {
}

func (DeploymentState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentState)(nil)).Elem()
}

type deploymentArgs struct {
	Disks             []Disk      `pulumi:"disks"`
	Name              string      `pulumi:"name"`
	Network_name      *string     `pulumi:"network_name"`
	Node_id           interface{} `pulumi:"node_id"`
	Qsfs              []QSFSInput `pulumi:"qsfs"`
	Solution_provider *int        `pulumi:"solution_provider"`
	Solution_type     *string     `pulumi:"solution_type"`
	Vms               []VMInput   `pulumi:"vms"`
	Zdbs              []ZDBInput  `pulumi:"zdbs"`
}

// The set of arguments for constructing a Deployment resource.
type DeploymentArgs struct {
	Disks             DiskArrayInput
	Name              pulumi.StringInput
	Network_name      pulumi.StringPtrInput
	Node_id           pulumi.Input
	Qsfs              QSFSInputArrayInput
	Solution_provider pulumi.IntPtrInput
	Solution_type     pulumi.StringPtrInput
	Vms               VMInputArrayInput
	Zdbs              ZDBInputArrayInput
}

func (DeploymentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentArgs)(nil)).Elem()
}

type DeploymentInput interface {
	pulumi.Input

	ToDeploymentOutput() DeploymentOutput
	ToDeploymentOutputWithContext(ctx context.Context) DeploymentOutput
}

func (*Deployment) ElementType() reflect.Type {
	return reflect.TypeOf((**Deployment)(nil)).Elem()
}

func (i *Deployment) ToDeploymentOutput() DeploymentOutput {
	return i.ToDeploymentOutputWithContext(context.Background())
}

func (i *Deployment) ToDeploymentOutputWithContext(ctx context.Context) DeploymentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentOutput)
}

func (i *Deployment) ToOutput(ctx context.Context) pulumix.Output[*Deployment] {
	return pulumix.Output[*Deployment]{
		OutputState: i.ToDeploymentOutputWithContext(ctx).OutputState,
	}
}

type DeploymentOutput struct{ *pulumi.OutputState }

func (DeploymentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Deployment)(nil)).Elem()
}

func (o DeploymentOutput) ToDeploymentOutput() DeploymentOutput {
	return o
}

func (o DeploymentOutput) ToDeploymentOutputWithContext(ctx context.Context) DeploymentOutput {
	return o
}

func (o DeploymentOutput) ToOutput(ctx context.Context) pulumix.Output[*Deployment] {
	return pulumix.Output[*Deployment]{
		OutputState: o.OutputState,
	}
}

func (o DeploymentOutput) Contract_id() pulumi.IntOutput {
	return o.ApplyT(func(v *Deployment) pulumi.IntOutput { return v.Contract_id }).(pulumi.IntOutput)
}

func (o DeploymentOutput) Disks() DiskArrayOutput {
	return o.ApplyT(func(v *Deployment) DiskArrayOutput { return v.Disks }).(DiskArrayOutput)
}

func (o DeploymentOutput) Ip_range() pulumi.StringOutput {
	return o.ApplyT(func(v *Deployment) pulumi.StringOutput { return v.Ip_range }).(pulumi.StringOutput)
}

func (o DeploymentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Deployment) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o DeploymentOutput) Network_name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Deployment) pulumi.StringPtrOutput { return v.Network_name }).(pulumi.StringPtrOutput)
}

func (o DeploymentOutput) Node_deployment_id() pulumi.IntMapOutput {
	return o.ApplyT(func(v *Deployment) pulumi.IntMapOutput { return v.Node_deployment_id }).(pulumi.IntMapOutput)
}

func (o DeploymentOutput) Node_id() pulumi.AnyOutput {
	return o.ApplyT(func(v *Deployment) pulumi.AnyOutput { return v.Node_id }).(pulumi.AnyOutput)
}

func (o DeploymentOutput) Qsfs() QSFSInputArrayOutput {
	return o.ApplyT(func(v *Deployment) QSFSInputArrayOutput { return v.Qsfs }).(QSFSInputArrayOutput)
}

func (o DeploymentOutput) Qsfs_computed() QSFSComputedArrayOutput {
	return o.ApplyT(func(v *Deployment) QSFSComputedArrayOutput { return v.Qsfs_computed }).(QSFSComputedArrayOutput)
}

func (o DeploymentOutput) Solution_provider() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Deployment) pulumi.IntPtrOutput { return v.Solution_provider }).(pulumi.IntPtrOutput)
}

func (o DeploymentOutput) Solution_type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Deployment) pulumi.StringPtrOutput { return v.Solution_type }).(pulumi.StringPtrOutput)
}

func (o DeploymentOutput) Vms() VMInputArrayOutput {
	return o.ApplyT(func(v *Deployment) VMInputArrayOutput { return v.Vms }).(VMInputArrayOutput)
}

func (o DeploymentOutput) Vms_computed() VMComputedArrayOutput {
	return o.ApplyT(func(v *Deployment) VMComputedArrayOutput { return v.Vms_computed }).(VMComputedArrayOutput)
}

func (o DeploymentOutput) Zdbs() ZDBInputArrayOutput {
	return o.ApplyT(func(v *Deployment) ZDBInputArrayOutput { return v.Zdbs }).(ZDBInputArrayOutput)
}

func (o DeploymentOutput) Zdbs_computed() ZDBComputedArrayOutput {
	return o.ApplyT(func(v *Deployment) ZDBComputedArrayOutput { return v.Zdbs_computed }).(ZDBComputedArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentInput)(nil)).Elem(), &Deployment{})
	pulumi.RegisterOutputType(DeploymentOutput{})
}
