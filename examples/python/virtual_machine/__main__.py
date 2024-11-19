import os
import random
import string
import pulumi
import pulumi_threefold as threefold

mnemonic = os.environ['MNEMONIC']
network = os.environ['NETWORK']
rand_str = ''.join(random.sample(string.ascii_lowercase, 8))

provider = threefold.Provider("provider", mnemonic=mnemonic, network=network)
scheduler = threefold.Scheduler("scheduler", farm_ids=[1],
opts=pulumi.ResourceOptions(provider=provider))
network = threefold.Network("network",
    name=f"net_{rand_str}",
    description="test network",
    nodes=[scheduler.nodes[0]],
    ip_range="10.1.0.0/16",
    mycelium=True,
    opts=pulumi.ResourceOptions(provider=provider,
        depends_on=[scheduler]))

deployment = threefold.Deployment("deployment",
    node_id=scheduler.nodes[0],
    name=f"deployment_{rand_str}",
    network_name=f"net_{rand_str}",
    vms=[threefold.VMInputArgs(
        name="vm",
        node_id=scheduler.nodes[0],
        flist="https://hub.grid.tf/tf-official-apps/base:latest.flist",
        entrypoint="/sbin/zinit init",
        network_name=f"net_{rand_str}",
        cpu=2,
        memory=256, #MB
        mycelium=True,
        mounts=[threefold.MountArgs(
            name="data",
            mount_point="/app",
        )],
        env_vars={
            "SSH_KEY": None,
        },
    )],
    disks=[threefold.DiskArgs(
        name="data",
        size=2,
    )],
    opts=pulumi.ResourceOptions(provider=provider,
        depends_on=[network]))

pulumi.export("node_deployment_id", deployment.node_deployment_id)
pulumi.export("planetary_ip", deployment.vms_computed[0].planetary_ip)
pulumi.export("mycelium_ip", deployment.vms_computed[0].mycelium_ip)
