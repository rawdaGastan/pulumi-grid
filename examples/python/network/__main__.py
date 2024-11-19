import os
import random
import string
import pulumi
import pulumi_threefold as threefold

mnemonic = os.environ['MNEMONIC']
network = os.environ['NETWORK']

provider = threefold.Provider("provider", mnemonic=mnemonic, network=network)
scheduler = threefold.Scheduler("scheduler", farm_ids=[1],
opts=pulumi.ResourceOptions(provider=provider))
network = threefold.Network("network",
    name=f"net_{''.join(random.sample(string.ascii_lowercase, 8))}",
    description="test network",
    nodes=[scheduler.nodes[0]],
    ip_range="10.1.0.0/16",
    mycelium=True,
    opts=pulumi.ResourceOptions(provider=provider,
        depends_on=[scheduler]))
pulumi.export("node_deployment_id", network.node_deployment_id)
pulumi.export("nodes_ip_range", network.nodes_ip_range)
