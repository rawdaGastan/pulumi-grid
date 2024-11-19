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
			Mru: pulumi.Int(1),
			Sru: pulumi.Int(2),
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
		deployment, err := threefold.NewDeployment(ctx, "deployment", &threefold.DeploymentArgs{
			Node_id: scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
				return nodes[0], nil
			}).(pulumi.IntOutput),
			Name:         pulumi.String("deployment_" + randStr),
			Network_name: pulumi.String("net_" + randStr),
			Vms: threefold.VMInputArray{
				&threefold.VMInputArgs{
					Name: pulumi.String("vm_" + randStr),
					Node_id: scheduler.Nodes.ApplyT(func(nodes []int) (int, error) {
						return nodes[0], nil
					}).(pulumi.IntOutput),
					Flist:        pulumi.String("https://hub.grid.tf/tf-official-apps/base:latest.flist"),
					Entrypoint:   pulumi.String("/sbin/zinit init"),
					Network_name: pulumi.String("net_" + randStr),
					Cpu:          pulumi.Int(2),
					Memory:       pulumi.Int(256),
					Planetary:    pulumi.Bool(true),
					Mycelium:     pulumi.Bool(true),
					Mounts: threefold.MountArray{
						&threefold.MountArgs{
							Name:        pulumi.String("data"),
							Mount_point: pulumi.String("/app"),
						},
					},
					Env_vars: pulumi.StringMap{
						"SSH_KEY": nil,
					},
				},
			},
			Disks: threefold.DiskArray{
				&threefold.DiskArgs{
					Name: pulumi.String("data"),
					Size: pulumi.Int(2),
				},
			},
		}, pulumi.Provider(tfProvider), pulumi.DependsOn([]pulumi.Resource{
			network,
		}))
		if err != nil {
			return err
		}
		ctx.Export("node_deployment_id", deployment.Node_deployment_id)
		ctx.Export("planetary_ip", deployment.Vms_computed.ApplyT(func(vms_computed []threefold.VMComputed) (*string, error) {
			return &vms_computed[0].Planetary_ip, nil
		}).(pulumi.StringPtrOutput))
		ctx.Export("mycelium_ip", deployment.Vms_computed.ApplyT(func(vms_computed []threefold.VMComputed) (*string, error) {
			return &vms_computed[0].Mycelium_ip, nil
		}).(pulumi.StringPtrOutput))
		return nil
	})
}
