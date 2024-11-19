import os
import random
import string
import pulumi
import pulumi_threefold as threefold

mnemonic = os.environ['MNEMONIC']
network = os.environ['NETWORK']
rand_str = ''.join(random.sample(string.ascii_lowercase, 8))

provider = threefold.Provider("provider", mnemonic=mnemonic, network=network)
scheduler = threefold.Scheduler("scheduler",
    mru=6,
    sru=6,
    farm_ids=[1],
    opts = pulumi.ResourceOptions(provider=provider))
network = threefold.Network("network",
    name=f"net_{rand_str}",
    description="test network",
    nodes=[scheduler.nodes[0]],
    ip_range="10.1.0.0/16",
    mycelium=True,
    opts = pulumi.ResourceOptions(provider=provider,
        depends_on=[scheduler]))
kubernetes = threefold.Kubernetes("kubernetes",
    master=threefold.K8sNodeInputArgs(
        name=f"kubernetes_{rand_str}",
        network_name=f"net_{rand_str}",
        node_id=scheduler.nodes[0],
        disk_size=2,
        planetary=True,
        mycelium=True,
        cpu=2,
        memory=2048,
    ),
    workers=[
        threefold.K8sNodeInputArgs(
            name=f"worker1_{rand_str}",
            network_name=f"net_{rand_str}",
            node_id=scheduler.nodes[0],
            disk_size=2,
            cpu=2,
            memory=2048,
            mycelium=True,
        ),
        threefold.K8sNodeInputArgs(
            name=f"worker2_{rand_str}",
            network_name=f"net_{rand_str}",
            node_id=scheduler.nodes[0],
            disk_size=2,
            cpu=2,
            memory=2048,
            mycelium=True,
        ),
    ],
    token="t123456789",
    network_name=f"net_{rand_str}",
    ssh_key=None,
    opts = pulumi.ResourceOptions(provider=provider,
        depends_on=[network]))

pulumi.export("node_deployment_id", kubernetes.node_deployment_id)
pulumi.export("master", kubernetes.master_computed)
