# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NetworkArgs', 'Network']

@pulumi.input_type
class NetworkArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 ip_range: pulumi.Input[str],
                 name: pulumi.Input[str],
                 nodes: pulumi.Input[Sequence[Any]],
                 add_wg_access: Optional[pulumi.Input[bool]] = None,
                 mycelium_keys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Network resource.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "ip_range", ip_range)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "nodes", nodes)
        if add_wg_access is not None:
            pulumi.set(__self__, "add_wg_access", add_wg_access)
        if mycelium_keys is not None:
            pulumi.set(__self__, "mycelium_keys", mycelium_keys)
        if solution_type is None:
            solution_type = 'Network'
        if solution_type is not None:
            pulumi.set(__self__, "solution_type", solution_type)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def ip_range(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ip_range")

    @ip_range.setter
    def ip_range(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_range", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Input[Sequence[Any]]:
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: pulumi.Input[Sequence[Any]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter
    def add_wg_access(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "add_wg_access")

    @add_wg_access.setter
    def add_wg_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_wg_access", value)

    @property
    @pulumi.getter
    def mycelium_keys(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "mycelium_keys")

    @mycelium_keys.setter
    def mycelium_keys(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "mycelium_keys", value)

    @property
    @pulumi.getter
    def solution_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "solution_type")

    @solution_type.setter
    def solution_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_type", value)


class Network(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_wg_access: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_range: Optional[pulumi.Input[str]] = None,
                 mycelium_keys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[Any]]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Network resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Network resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param NetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_wg_access: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_range: Optional[pulumi.Input[str]] = None,
                 mycelium_keys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[Any]]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkArgs.__new__(NetworkArgs)

            __props__.__dict__["add_wg_access"] = add_wg_access
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if ip_range is None and not opts.urn:
                raise TypeError("Missing required property 'ip_range'")
            __props__.__dict__["ip_range"] = ip_range
            __props__.__dict__["mycelium_keys"] = mycelium_keys
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if nodes is None and not opts.urn:
                raise TypeError("Missing required property 'nodes'")
            __props__.__dict__["nodes"] = nodes
            if solution_type is None:
                solution_type = 'Network'
            __props__.__dict__["solution_type"] = solution_type
            __props__.__dict__["access_wg_config"] = None
            __props__.__dict__["external_ip"] = None
            __props__.__dict__["external_sk"] = None
            __props__.__dict__["node_deployment_id"] = None
            __props__.__dict__["nodes_ip_range"] = None
            __props__.__dict__["public_node_id"] = None
        super(Network, __self__).__init__(
            'threefold:provider:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Network':
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkArgs.__new__(NetworkArgs)

        __props__.__dict__["access_wg_config"] = None
        __props__.__dict__["add_wg_access"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["external_ip"] = None
        __props__.__dict__["external_sk"] = None
        __props__.__dict__["ip_range"] = None
        __props__.__dict__["mycelium_keys"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_deployment_id"] = None
        __props__.__dict__["nodes"] = None
        __props__.__dict__["nodes_ip_range"] = None
        __props__.__dict__["public_node_id"] = None
        __props__.__dict__["solution_type"] = None
        return Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def access_wg_config(self) -> pulumi.Output[str]:
        return pulumi.get(self, "access_wg_config")

    @property
    @pulumi.getter
    def add_wg_access(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "add_wg_access")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def external_ip(self) -> pulumi.Output[str]:
        return pulumi.get(self, "external_ip")

    @property
    @pulumi.getter
    def external_sk(self) -> pulumi.Output[str]:
        return pulumi.get(self, "external_sk")

    @property
    @pulumi.getter
    def ip_range(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter
    def mycelium_keys(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "mycelium_keys")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def node_deployment_id(self) -> pulumi.Output[Mapping[str, int]]:
        return pulumi.get(self, "node_deployment_id")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence[Any]]:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter
    def nodes_ip_range(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "nodes_ip_range")

    @property
    @pulumi.getter
    def public_node_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "public_node_id")

    @property
    @pulumi.getter
    def solution_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "solution_type")

