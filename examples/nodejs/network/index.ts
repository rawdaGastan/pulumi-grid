import * as threefold from "@threefold/pulumi";

var rand_str = Math.random().toString(36).slice(8)

const provider = new threefold.Provider("provider", {mnemonic: process.env.MNEMONIC, network: process.env.NETWORK});
const scheduler = new threefold.Scheduler("scheduler", {farm_ids: [1], ygg: true}, {
    provider: provider,
});
const network = new threefold.Network("network", {
    name: "net_"+rand_str,
    description: "test network",
    nodes: [scheduler.nodes[0]],
    ip_range: "10.1.0.0/16",
		mycelium: true,
}, {
    provider: provider,
    dependsOn: [scheduler],
});
export const nodeDeploymentId = network.node_deployment_id;
export const nodesIpRange = network.nodes_ip_range;
