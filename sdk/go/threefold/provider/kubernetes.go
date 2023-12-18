// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package provider

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/threefoldtech/pulumi-threefold/sdk/go/threefold/internal"
)

type Kubernetes struct {
	pulumi.CustomResourceState

	Master             K8sNodeInputOutput       `pulumi:"master"`
	Master_computed    K8sNodeComputedOutput    `pulumi:"master_computed"`
	Network_name       pulumi.StringOutput      `pulumi:"network_name"`
	Node_deployment_id pulumi.IntMapOutput      `pulumi:"node_deployment_id"`
	Nodes_ip_range     pulumi.StringMapOutput   `pulumi:"nodes_ip_range"`
	Solution_type      pulumi.StringPtrOutput   `pulumi:"solution_type"`
	Ssh_key            pulumi.StringPtrOutput   `pulumi:"ssh_key"`
	Token              pulumi.StringOutput      `pulumi:"token"`
	Workers            K8sNodeInputArrayOutput  `pulumi:"workers"`
	Workers_computed   K8sNodeComputedMapOutput `pulumi:"workers_computed"`
}

// NewKubernetes registers a new resource with the given unique name, arguments, and options.
func NewKubernetes(ctx *pulumi.Context,
	name string, args *KubernetesArgs, opts ...pulumi.ResourceOption) (*Kubernetes, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Master == nil {
		return nil, errors.New("invalid value for required argument 'Master'")
	}
	if args.Network_name == nil {
		return nil, errors.New("invalid value for required argument 'Network_name'")
	}
	if args.Token == nil {
		return nil, errors.New("invalid value for required argument 'Token'")
	}
	if args.Workers == nil {
		return nil, errors.New("invalid value for required argument 'Workers'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Kubernetes
	err := ctx.RegisterResource("threefold:provider:Kubernetes", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKubernetes gets an existing Kubernetes resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKubernetes(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KubernetesState, opts ...pulumi.ResourceOption) (*Kubernetes, error) {
	var resource Kubernetes
	err := ctx.ReadResource("threefold:provider:Kubernetes", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Kubernetes resources.
type kubernetesState struct {
}

type KubernetesState struct {
}

func (KubernetesState) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesState)(nil)).Elem()
}

type kubernetesArgs struct {
	Master        K8sNodeInput   `pulumi:"master"`
	Network_name  string         `pulumi:"network_name"`
	Solution_type *string        `pulumi:"solution_type"`
	Ssh_key       *string        `pulumi:"ssh_key"`
	Token         string         `pulumi:"token"`
	Workers       []K8sNodeInput `pulumi:"workers"`
}

// The set of arguments for constructing a Kubernetes resource.
type KubernetesArgs struct {
	Master        K8sNodeInputInput
	Network_name  pulumi.StringInput
	Solution_type pulumi.StringPtrInput
	Ssh_key       pulumi.StringPtrInput
	Token         pulumi.StringInput
	Workers       K8sNodeInputArrayInput
}

func (KubernetesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesArgs)(nil)).Elem()
}

type KubernetesInput interface {
	pulumi.Input

	ToKubernetesOutput() KubernetesOutput
	ToKubernetesOutputWithContext(ctx context.Context) KubernetesOutput
}

func (*Kubernetes) ElementType() reflect.Type {
	return reflect.TypeOf((**Kubernetes)(nil)).Elem()
}

func (i *Kubernetes) ToKubernetesOutput() KubernetesOutput {
	return i.ToKubernetesOutputWithContext(context.Background())
}

func (i *Kubernetes) ToKubernetesOutputWithContext(ctx context.Context) KubernetesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesOutput)
}

// KubernetesArrayInput is an input type that accepts KubernetesArray and KubernetesArrayOutput values.
// You can construct a concrete instance of `KubernetesArrayInput` via:
//
//	KubernetesArray{ KubernetesArgs{...} }
type KubernetesArrayInput interface {
	pulumi.Input

	ToKubernetesArrayOutput() KubernetesArrayOutput
	ToKubernetesArrayOutputWithContext(context.Context) KubernetesArrayOutput
}

type KubernetesArray []KubernetesInput

func (KubernetesArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Kubernetes)(nil)).Elem()
}

func (i KubernetesArray) ToKubernetesArrayOutput() KubernetesArrayOutput {
	return i.ToKubernetesArrayOutputWithContext(context.Background())
}

func (i KubernetesArray) ToKubernetesArrayOutputWithContext(ctx context.Context) KubernetesArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesArrayOutput)
}

// KubernetesMapInput is an input type that accepts KubernetesMap and KubernetesMapOutput values.
// You can construct a concrete instance of `KubernetesMapInput` via:
//
//	KubernetesMap{ "key": KubernetesArgs{...} }
type KubernetesMapInput interface {
	pulumi.Input

	ToKubernetesMapOutput() KubernetesMapOutput
	ToKubernetesMapOutputWithContext(context.Context) KubernetesMapOutput
}

type KubernetesMap map[string]KubernetesInput

func (KubernetesMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Kubernetes)(nil)).Elem()
}

func (i KubernetesMap) ToKubernetesMapOutput() KubernetesMapOutput {
	return i.ToKubernetesMapOutputWithContext(context.Background())
}

func (i KubernetesMap) ToKubernetesMapOutputWithContext(ctx context.Context) KubernetesMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesMapOutput)
}

type KubernetesOutput struct{ *pulumi.OutputState }

func (KubernetesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Kubernetes)(nil)).Elem()
}

func (o KubernetesOutput) ToKubernetesOutput() KubernetesOutput {
	return o
}

func (o KubernetesOutput) ToKubernetesOutputWithContext(ctx context.Context) KubernetesOutput {
	return o
}

func (o KubernetesOutput) Master() K8sNodeInputOutput {
	return o.ApplyT(func(v *Kubernetes) K8sNodeInputOutput { return v.Master }).(K8sNodeInputOutput)
}

func (o KubernetesOutput) Master_computed() K8sNodeComputedOutput {
	return o.ApplyT(func(v *Kubernetes) K8sNodeComputedOutput { return v.Master_computed }).(K8sNodeComputedOutput)
}

func (o KubernetesOutput) Network_name() pulumi.StringOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.StringOutput { return v.Network_name }).(pulumi.StringOutput)
}

func (o KubernetesOutput) Node_deployment_id() pulumi.IntMapOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.IntMapOutput { return v.Node_deployment_id }).(pulumi.IntMapOutput)
}

func (o KubernetesOutput) Nodes_ip_range() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.StringMapOutput { return v.Nodes_ip_range }).(pulumi.StringMapOutput)
}

func (o KubernetesOutput) Solution_type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.StringPtrOutput { return v.Solution_type }).(pulumi.StringPtrOutput)
}

func (o KubernetesOutput) Ssh_key() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.StringPtrOutput { return v.Ssh_key }).(pulumi.StringPtrOutput)
}

func (o KubernetesOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v *Kubernetes) pulumi.StringOutput { return v.Token }).(pulumi.StringOutput)
}

func (o KubernetesOutput) Workers() K8sNodeInputArrayOutput {
	return o.ApplyT(func(v *Kubernetes) K8sNodeInputArrayOutput { return v.Workers }).(K8sNodeInputArrayOutput)
}

func (o KubernetesOutput) Workers_computed() K8sNodeComputedMapOutput {
	return o.ApplyT(func(v *Kubernetes) K8sNodeComputedMapOutput { return v.Workers_computed }).(K8sNodeComputedMapOutput)
}

type KubernetesArrayOutput struct{ *pulumi.OutputState }

func (KubernetesArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Kubernetes)(nil)).Elem()
}

func (o KubernetesArrayOutput) ToKubernetesArrayOutput() KubernetesArrayOutput {
	return o
}

func (o KubernetesArrayOutput) ToKubernetesArrayOutputWithContext(ctx context.Context) KubernetesArrayOutput {
	return o
}

func (o KubernetesArrayOutput) Index(i pulumi.IntInput) KubernetesOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Kubernetes {
		return vs[0].([]*Kubernetes)[vs[1].(int)]
	}).(KubernetesOutput)
}

type KubernetesMapOutput struct{ *pulumi.OutputState }

func (KubernetesMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Kubernetes)(nil)).Elem()
}

func (o KubernetesMapOutput) ToKubernetesMapOutput() KubernetesMapOutput {
	return o
}

func (o KubernetesMapOutput) ToKubernetesMapOutputWithContext(ctx context.Context) KubernetesMapOutput {
	return o
}

func (o KubernetesMapOutput) MapIndex(k pulumi.StringInput) KubernetesOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Kubernetes {
		return vs[0].(map[string]*Kubernetes)[vs[1].(string)]
	}).(KubernetesOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesInput)(nil)).Elem(), &Kubernetes{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesArrayInput)(nil)).Elem(), KubernetesArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesMapInput)(nil)).Elem(), KubernetesMap{})
	pulumi.RegisterOutputType(KubernetesOutput{})
	pulumi.RegisterOutputType(KubernetesArrayOutput{})
	pulumi.RegisterOutputType(KubernetesMapOutput{})
}
