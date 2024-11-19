package main

import (
	"encoding/base64"
	"os"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/threefoldtech/pulumi-threefold/sdk/go/threefold"
	"golang.org/x/exp/rand"
)

func randomString() string {
	bytes := make([]byte, 8)
	rand.Read(bytes)
	return base64.URLEncoding.EncodeToString(bytes)[:8]
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		tfProvider, err := threefold.NewProvider(ctx, "provider", &threefold.ProviderArgs{
			Mnemonic: pulumi.String(os.Getenv("MNEMONIC")),
		})
		if err != nil {
			return err
		}

		scheduler, err := threefold.NewScheduler(ctx, "scheduler", &threefold.SchedulerArgs{
			Farm_ids: pulumi.IntArray{
				pulumi.Int(1),
			},
		}, pulumi.Provider(tfProvider))
		if err != nil {
			return err
		}

		network, err := threefold.NewNetwork(ctx, "network", &threefold.NetworkArgs{
			Name:        pulumi.String("net_" + randomString()),
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

		ctx.Export("node_deployment_id", network.Node_deployment_id)
		ctx.Export("nodes_ip_range", network.Nodes_ip_range)
		return nil
	})
}
