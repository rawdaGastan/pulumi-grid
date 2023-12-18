# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GatewayFQDNArgs', 'GatewayFQDN']

@pulumi.input_type
class GatewayFQDNArgs:
    def __init__(__self__, *,
                 backends: pulumi.Input[Sequence[pulumi.Input[str]]],
                 fqdn: pulumi.Input[str],
                 name: pulumi.Input[str],
                 node_id: Any,
                 description: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 tls_pass_through: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GatewayFQDN resource.
        """
        pulumi.set(__self__, "backends", backends)
        pulumi.set(__self__, "fqdn", fqdn)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "node_id", node_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if network_name is not None:
            pulumi.set(__self__, "network_name", network_name)
        if solution_type is not None:
            pulumi.set(__self__, "solution_type", solution_type)
        if tls_pass_through is not None:
            pulumi.set(__self__, "tls_pass_through", tls_pass_through)

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "backends", value)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: pulumi.Input[str]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def node_id(self) -> Any:
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Any):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def network_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def solution_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "solution_type")

    @solution_type.setter
    def solution_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_type", value)

    @property
    @pulumi.getter
    def tls_pass_through(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "tls_pass_through")

    @tls_pass_through.setter
    def tls_pass_through(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tls_pass_through", value)


class GatewayFQDN(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[Any] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 tls_pass_through: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a GatewayFQDN resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayFQDNArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a GatewayFQDN resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param GatewayFQDNArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayFQDNArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[Any] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 tls_pass_through: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayFQDNArgs.__new__(GatewayFQDNArgs)

            if backends is None and not opts.urn:
                raise TypeError("Missing required property 'backends'")
            __props__.__dict__["backends"] = backends
            __props__.__dict__["description"] = description
            if fqdn is None and not opts.urn:
                raise TypeError("Missing required property 'fqdn'")
            __props__.__dict__["fqdn"] = fqdn
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["network_name"] = network_name
            if node_id is None and not opts.urn:
                raise TypeError("Missing required property 'node_id'")
            __props__.__dict__["node_id"] = node_id
            __props__.__dict__["solution_type"] = solution_type
            __props__.__dict__["tls_pass_through"] = tls_pass_through
            __props__.__dict__["contract_id"] = None
            __props__.__dict__["node_deployment_id"] = None
        super(GatewayFQDN, __self__).__init__(
            'threefold:provider:GatewayFQDN',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GatewayFQDN':
        """
        Get an existing GatewayFQDN resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayFQDNArgs.__new__(GatewayFQDNArgs)

        __props__.__dict__["backends"] = None
        __props__.__dict__["contract_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_name"] = None
        __props__.__dict__["node_deployment_id"] = None
        __props__.__dict__["node_id"] = None
        __props__.__dict__["solution_type"] = None
        __props__.__dict__["tls_pass_through"] = None
        return GatewayFQDN(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "backends")

    @property
    @pulumi.getter
    def contract_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "contract_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter
    def node_deployment_id(self) -> pulumi.Output[Mapping[str, int]]:
        return pulumi.get(self, "node_deployment_id")

    @property
    @pulumi.getter
    def node_id(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def solution_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "solution_type")

    @property
    @pulumi.getter
    def tls_pass_through(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "tls_pass_through")

