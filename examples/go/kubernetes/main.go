package main

import (
	"crypto/rand"
	"encoding/base64"
	"os"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/threefoldtech/pulumi-threefold/sdk/go/threefold"
)

func randomString() string {
	bytes := make([]byte, 8)
	rand.Read(bytes)
	return base64.URLEncoding.EncodeToString(bytes)[:8]
}

func main() {
	randStr := randomString()
	pulumi.Run(func(ctx *pulumi.Context) error {
		tfProvider, err := threefold.NewProvider(ctx, "provider", &threefold.ProviderArgs{
			Mnemonic: pulumi.String(os.Getenv("MNEMONIC")),
		})
		if err != nil {
			return err
		}
		scheduler, err := threefold.NewScheduler(ctx, "scheduler", &threefold.SchedulerArgs{
			Mru: pulumi.Int(6),
			Sru: pulumi.Int(6),
			Farm_ids: pulumi.IntArray{
				pulumi.Int(1),
			},
		}, pulumi.Provider(tfProvider))
		if err != nil {
			return err
		}
		network, err := threefold.NewNetwork(ctx, "network", &threefold.NetworkArgs{
			Name:        pulumi.String("net_" + randStr),
			Description: pulumi.String("test network"),
			Nodes: pulumi.Array{
				scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
					return nodes[0], nil
				}).(pulumi.IntOutput),
			},
			Ip_range: pulumi.String("10.1.0.0/16"),
			Mycelium: pulumi.Bool(true),
		}, pulumi.Provider(tfProvider), pulumi.DependsOn([]pulumi.Resource{
			scheduler,
		}))
		if err != nil {
			return err
		}
		kubernetes, err := threefold.NewKubernetes(ctx, "kubernetes", &threefold.KubernetesArgs{
			Master: &threefold.K8sNodeInputArgs{
				Name:         pulumi.String("kubernetes_" + randStr),
				Network_name: pulumi.String("net_" + randStr),
				Node_id: scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
					return nodes[0], nil
				}).(pulumi.IntOutput),
				Planetary: pulumi.Bool(true),
				Mycelium:  pulumi.Bool(true),
				Cpu:       pulumi.Int(2),
				Memory:    pulumi.Int(2048),
				Disk_size: pulumi.Int(2),
			},
			Workers: threefold.K8sNodeInputArray{
				&threefold.K8sNodeInputArgs{
					Name:         pulumi.String("worker1_" + randStr),
					Network_name: pulumi.String("net_" + randStr),
					Node_id: scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
						return nodes[0], nil
					}).(pulumi.IntOutput),
					Cpu:       pulumi.Int(2),
					Memory:    pulumi.Int(2048),
					Disk_size: pulumi.Int(2),
				},
				&threefold.K8sNodeInputArgs{
					Name:         pulumi.String("worker2_" + randStr),
					Network_name: pulumi.String("net_" + randStr),
					Node_id: scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
						return nodes[0], nil
					}).(pulumi.IntOutput),
					Cpu:       pulumi.Int(2),
					Memory:    pulumi.Int(2048),
					Disk_size: pulumi.Int(2),
				},
			},
			Token:        pulumi.String("t123456789"),
			Network_name: pulumi.String("net_" + randStr),
			Ssh_key:      nil,
		}, pulumi.Provider(tfProvider), pulumi.DependsOn([]pulumi.Resource{
			network,
		}))
		if err != nil {
			return err
		}
		ctx.Export("node_deployment_id", kubernetes.Node_deployment_id)
		ctx.Export("planetary_ip", kubernetes.Master_computed.ApplyT(func(master_computed threefold.VMComputed) (*string, error) {
			return &master_computed.Planetary_ip, nil
		}).(pulumi.StringPtrOutput))
		ctx.Export("mycelium_ip", kubernetes.Master_computed.ApplyT(func(master_computed threefold.VMComputed) (*string, error) {
			return &master_computed.Mycelium_ip, nil
		}).(pulumi.StringPtrOutput))
		return nil
	})
}
