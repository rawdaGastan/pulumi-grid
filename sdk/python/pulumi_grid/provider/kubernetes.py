# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KubernetesArgs', 'Kubernetes']

@pulumi.input_type
class KubernetesArgs:
    def __init__(__self__, *,
                 master: pulumi.Input['K8sNodeInputArgs'],
                 network_name: pulumi.Input[str],
                 token: pulumi.Input[str],
                 workers: pulumi.Input[Sequence[pulumi.Input['K8sNodeInputArgs']]],
                 solution_type: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Kubernetes resource.
        """
        pulumi.set(__self__, "master", master)
        pulumi.set(__self__, "network_name", network_name)
        pulumi.set(__self__, "token", token)
        pulumi.set(__self__, "workers", workers)
        if solution_type is not None:
            pulumi.set(__self__, "solution_type", solution_type)
        if ssh_key is not None:
            pulumi.set(__self__, "ssh_key", ssh_key)

    @property
    @pulumi.getter
    def master(self) -> pulumi.Input['K8sNodeInputArgs']:
        return pulumi.get(self, "master")

    @master.setter
    def master(self, value: pulumi.Input['K8sNodeInputArgs']):
        pulumi.set(self, "master", value)

    @property
    @pulumi.getter
    def network_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def workers(self) -> pulumi.Input[Sequence[pulumi.Input['K8sNodeInputArgs']]]:
        return pulumi.get(self, "workers")

    @workers.setter
    def workers(self, value: pulumi.Input[Sequence[pulumi.Input['K8sNodeInputArgs']]]):
        pulumi.set(self, "workers", value)

    @property
    @pulumi.getter
    def solution_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "solution_type")

    @solution_type.setter
    def solution_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_type", value)

    @property
    @pulumi.getter
    def ssh_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssh_key")

    @ssh_key.setter
    def ssh_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_key", value)


class Kubernetes(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 master: Optional[pulumi.Input[pulumi.InputType['K8sNodeInputArgs']]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 workers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['K8sNodeInputArgs']]]]] = None,
                 __props__=None):
        """
        Create a Kubernetes resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Kubernetes resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KubernetesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubernetesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 master: Optional[pulumi.Input[pulumi.InputType['K8sNodeInputArgs']]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 workers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['K8sNodeInputArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubernetesArgs.__new__(KubernetesArgs)

            if master is None and not opts.urn:
                raise TypeError("Missing required property 'master'")
            __props__.__dict__["master"] = master
            if network_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_name'")
            __props__.__dict__["network_name"] = network_name
            __props__.__dict__["solution_type"] = solution_type
            __props__.__dict__["ssh_key"] = ssh_key
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = token
            if workers is None and not opts.urn:
                raise TypeError("Missing required property 'workers'")
            __props__.__dict__["workers"] = workers
            __props__.__dict__["master_computed"] = None
            __props__.__dict__["node_deployment_id"] = None
            __props__.__dict__["nodes_ip_range"] = None
            __props__.__dict__["workers_computed"] = None
        super(Kubernetes, __self__).__init__(
            'grid:provider:Kubernetes',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Kubernetes':
        """
        Get an existing Kubernetes resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KubernetesArgs.__new__(KubernetesArgs)

        __props__.__dict__["master"] = None
        __props__.__dict__["master_computed"] = None
        __props__.__dict__["network_name"] = None
        __props__.__dict__["node_deployment_id"] = None
        __props__.__dict__["nodes_ip_range"] = None
        __props__.__dict__["solution_type"] = None
        __props__.__dict__["ssh_key"] = None
        __props__.__dict__["token"] = None
        __props__.__dict__["workers"] = None
        __props__.__dict__["workers_computed"] = None
        return Kubernetes(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def master(self) -> pulumi.Output['outputs.K8sNodeInput']:
        return pulumi.get(self, "master")

    @property
    @pulumi.getter
    def master_computed(self) -> pulumi.Output['outputs.K8sNodeComputed']:
        return pulumi.get(self, "master_computed")

    @property
    @pulumi.getter
    def network_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter
    def node_deployment_id(self) -> pulumi.Output[Mapping[str, int]]:
        return pulumi.get(self, "node_deployment_id")

    @property
    @pulumi.getter
    def nodes_ip_range(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "nodes_ip_range")

    @property
    @pulumi.getter
    def solution_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "solution_type")

    @property
    @pulumi.getter
    def ssh_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssh_key")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def workers(self) -> pulumi.Output[Sequence['outputs.K8sNodeInput']]:
        return pulumi.get(self, "workers")

    @property
    @pulumi.getter
    def workers_computed(self) -> pulumi.Output[Mapping[str, 'outputs.K8sNodeComputed']]:
        return pulumi.get(self, "workers_computed")

