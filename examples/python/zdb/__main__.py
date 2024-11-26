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
    mru=0.25,
    sru=2,
    farm_ids=[1],
    ygg=True,
    opts = pulumi.ResourceOptions(provider=provider))
deployment = threefold.Deployment("deployment",
    node_id=scheduler.nodes[0],
    name=f"deployment_{rand_str}",
    zdbs=[threefold.ZDBInputArgs(
        name=f"zdb_{rand_str}",
        size=2,
        password="123456",
    )],
    opts = pulumi.ResourceOptions(provider=provider))

pulumi.export("node_deployment_id", deployment.node_deployment_id)
pulumi.export("zdb_endpoint_ip", deployment.zdbs_computed[0].ips[1])
pulumi.export("zdb_endpoint_port", deployment.zdbs_computed[0].port)
pulumi.export("zdb_namespace", deployment.zdbs_computed[0].namespace)
