# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'BackendArgs',
    'DiskArgs',
    'GroupArgs',
    'K8sNodeInputArgs',
    'MetadataArgs',
    'MountArgs',
    'QSFSInputArgs',
    'VMInputArgs',
    'ZDBInputArgs',
    'ZlogArgs',
]

@pulumi.input_type
class BackendArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 password: pulumi.Input[str]):
        BackendArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address=address,
            namespace=namespace,
            password=password,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address: Optional[pulumi.Input[str]] = None,
             namespace: Optional[pulumi.Input[str]] = None,
             password: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if address is None:
            raise TypeError("Missing 'address' argument")
        if namespace is None:
            raise TypeError("Missing 'namespace' argument")
        if password is None:
            raise TypeError("Missing 'password' argument")

        _setter("address", address)
        _setter("namespace", namespace)
        _setter("password", password)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 size: pulumi.Input[int],
                 description: Optional[pulumi.Input[str]] = None):
        DiskArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            size=size,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             size: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if size is None:
            raise TypeError("Missing 'size' argument")

        _setter("name", name)
        _setter("size", size)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]] = None):
        GroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            backends=backends,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             backends: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if backends is not None:
            _setter("backends", backends)

    @property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]]:
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]]):
        pulumi.set(self, "backends", value)


@pulumi.input_type
class K8sNodeInputArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[int],
                 disk_size: pulumi.Input[int],
                 memory: pulumi.Input[int],
                 name: pulumi.Input[str],
                 node: Any,
                 flist: Optional[pulumi.Input[str]] = None,
                 flist_checksum: Optional[pulumi.Input[str]] = None,
                 planetary: Optional[pulumi.Input[bool]] = None,
                 public_ip: Optional[pulumi.Input[bool]] = None,
                 public_ip6: Optional[pulumi.Input[bool]] = None):
        K8sNodeInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            disk_size=disk_size,
            memory=memory,
            name=name,
            node=node,
            flist=flist,
            flist_checksum=flist_checksum,
            planetary=planetary,
            public_ip=public_ip,
            public_ip6=public_ip6,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: Optional[pulumi.Input[int]] = None,
             disk_size: Optional[pulumi.Input[int]] = None,
             memory: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             node: Optional[Any] = None,
             flist: Optional[pulumi.Input[str]] = None,
             flist_checksum: Optional[pulumi.Input[str]] = None,
             planetary: Optional[pulumi.Input[bool]] = None,
             public_ip: Optional[pulumi.Input[bool]] = None,
             public_ip6: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if cpu is None:
            raise TypeError("Missing 'cpu' argument")
        if disk_size is None:
            raise TypeError("Missing 'disk_size' argument")
        if memory is None:
            raise TypeError("Missing 'memory' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if node is None:
            raise TypeError("Missing 'node' argument")

        _setter("cpu", cpu)
        _setter("disk_size", disk_size)
        _setter("memory", memory)
        _setter("name", name)
        _setter("node", node)
        if flist is not None:
            _setter("flist", flist)
        if flist_checksum is not None:
            _setter("flist_checksum", flist_checksum)
        if planetary is not None:
            _setter("planetary", planetary)
        if public_ip is not None:
            _setter("public_ip", public_ip)
        if public_ip6 is not None:
            _setter("public_ip6", public_ip6)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[int]:
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[int]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def disk_size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[int]:
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[int]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def node(self) -> Any:
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: Any):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter
    def flist(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "flist")

    @flist.setter
    def flist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flist", value)

    @property
    @pulumi.getter
    def flist_checksum(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "flist_checksum")

    @flist_checksum.setter
    def flist_checksum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flist_checksum", value)

    @property
    @pulumi.getter
    def planetary(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "planetary")

    @planetary.setter
    def planetary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "planetary", value)

    @property
    @pulumi.getter
    def public_ip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter
    def public_ip6(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_ip6")

    @public_ip6.setter
    def public_ip6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip6", value)


@pulumi.input_type
class MetadataArgs:
    def __init__(__self__, *,
                 encryption_key: pulumi.Input[str],
                 prefix: pulumi.Input[str],
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]] = None,
                 encryption_algorithm: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        MetadataArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encryption_key=encryption_key,
            prefix=prefix,
            backends=backends,
            encryption_algorithm=encryption_algorithm,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encryption_key: Optional[pulumi.Input[str]] = None,
             prefix: Optional[pulumi.Input[str]] = None,
             backends: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]] = None,
             encryption_algorithm: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if encryption_key is None:
            raise TypeError("Missing 'encryption_key' argument")
        if prefix is None:
            raise TypeError("Missing 'prefix' argument")

        _setter("encryption_key", encryption_key)
        _setter("prefix", prefix)
        if backends is not None:
            _setter("backends", backends)
        if encryption_algorithm is not None:
            _setter("encryption_algorithm", encryption_algorithm)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def encryption_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[str]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]]:
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackendArgs']]]]):
        pulumi.set(self, "backends", value)

    @property
    @pulumi.getter
    def encryption_algorithm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_algorithm")

    @encryption_algorithm.setter
    def encryption_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_algorithm", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class MountArgs:
    def __init__(__self__, *,
                 disk_name: pulumi.Input[str],
                 mount_point: pulumi.Input[str]):
        MountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            disk_name=disk_name,
            mount_point=mount_point,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             disk_name: Optional[pulumi.Input[str]] = None,
             mount_point: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if disk_name is None:
            raise TypeError("Missing 'disk_name' argument")
        if mount_point is None:
            raise TypeError("Missing 'mount_point' argument")

        _setter("disk_name", disk_name)
        _setter("mount_point", mount_point)

    @property
    @pulumi.getter
    def disk_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "disk_name")

    @disk_name.setter
    def disk_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "disk_name", value)

    @property
    @pulumi.getter
    def mount_point(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mount_point")

    @mount_point.setter
    def mount_point(self, value: pulumi.Input[str]):
        pulumi.set(self, "mount_point", value)


@pulumi.input_type
class QSFSInputArgs:
    def __init__(__self__, *,
                 cache: pulumi.Input[int],
                 encryption_key: pulumi.Input[str],
                 expected_shards: pulumi.Input[int],
                 groups: pulumi.Input[Sequence[pulumi.Input['GroupArgs']]],
                 max_zdb_data_dir_size: pulumi.Input[int],
                 metadata: pulumi.Input['MetadataArgs'],
                 minimal_shards: pulumi.Input[int],
                 name: pulumi.Input[str],
                 redundant_groups: pulumi.Input[int],
                 redundant_nodes: pulumi.Input[int],
                 compression_algorithm: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encryption_algorithm: Optional[pulumi.Input[str]] = None):
        QSFSInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cache=cache,
            encryption_key=encryption_key,
            expected_shards=expected_shards,
            groups=groups,
            max_zdb_data_dir_size=max_zdb_data_dir_size,
            metadata=metadata,
            minimal_shards=minimal_shards,
            name=name,
            redundant_groups=redundant_groups,
            redundant_nodes=redundant_nodes,
            compression_algorithm=compression_algorithm,
            description=description,
            encryption_algorithm=encryption_algorithm,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cache: Optional[pulumi.Input[int]] = None,
             encryption_key: Optional[pulumi.Input[str]] = None,
             expected_shards: Optional[pulumi.Input[int]] = None,
             groups: Optional[pulumi.Input[Sequence[pulumi.Input['GroupArgs']]]] = None,
             max_zdb_data_dir_size: Optional[pulumi.Input[int]] = None,
             metadata: Optional[pulumi.Input['MetadataArgs']] = None,
             minimal_shards: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             redundant_groups: Optional[pulumi.Input[int]] = None,
             redundant_nodes: Optional[pulumi.Input[int]] = None,
             compression_algorithm: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             encryption_algorithm: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if cache is None:
            raise TypeError("Missing 'cache' argument")
        if encryption_key is None:
            raise TypeError("Missing 'encryption_key' argument")
        if expected_shards is None:
            raise TypeError("Missing 'expected_shards' argument")
        if groups is None:
            raise TypeError("Missing 'groups' argument")
        if max_zdb_data_dir_size is None:
            raise TypeError("Missing 'max_zdb_data_dir_size' argument")
        if metadata is None:
            raise TypeError("Missing 'metadata' argument")
        if minimal_shards is None:
            raise TypeError("Missing 'minimal_shards' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if redundant_groups is None:
            raise TypeError("Missing 'redundant_groups' argument")
        if redundant_nodes is None:
            raise TypeError("Missing 'redundant_nodes' argument")

        _setter("cache", cache)
        _setter("encryption_key", encryption_key)
        _setter("expected_shards", expected_shards)
        _setter("groups", groups)
        _setter("max_zdb_data_dir_size", max_zdb_data_dir_size)
        _setter("metadata", metadata)
        _setter("minimal_shards", minimal_shards)
        _setter("name", name)
        _setter("redundant_groups", redundant_groups)
        _setter("redundant_nodes", redundant_nodes)
        if compression_algorithm is not None:
            _setter("compression_algorithm", compression_algorithm)
        if description is not None:
            _setter("description", description)
        if encryption_algorithm is not None:
            _setter("encryption_algorithm", encryption_algorithm)

    @property
    @pulumi.getter
    def cache(self) -> pulumi.Input[int]:
        return pulumi.get(self, "cache")

    @cache.setter
    def cache(self, value: pulumi.Input[int]):
        pulumi.set(self, "cache", value)

    @property
    @pulumi.getter
    def encryption_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def expected_shards(self) -> pulumi.Input[int]:
        return pulumi.get(self, "expected_shards")

    @expected_shards.setter
    def expected_shards(self, value: pulumi.Input[int]):
        pulumi.set(self, "expected_shards", value)

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input['GroupArgs']]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: pulumi.Input[Sequence[pulumi.Input['GroupArgs']]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter
    def max_zdb_data_dir_size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "max_zdb_data_dir_size")

    @max_zdb_data_dir_size.setter
    def max_zdb_data_dir_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_zdb_data_dir_size", value)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Input['MetadataArgs']:
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: pulumi.Input['MetadataArgs']):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def minimal_shards(self) -> pulumi.Input[int]:
        return pulumi.get(self, "minimal_shards")

    @minimal_shards.setter
    def minimal_shards(self, value: pulumi.Input[int]):
        pulumi.set(self, "minimal_shards", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def redundant_groups(self) -> pulumi.Input[int]:
        return pulumi.get(self, "redundant_groups")

    @redundant_groups.setter
    def redundant_groups(self, value: pulumi.Input[int]):
        pulumi.set(self, "redundant_groups", value)

    @property
    @pulumi.getter
    def redundant_nodes(self) -> pulumi.Input[int]:
        return pulumi.get(self, "redundant_nodes")

    @redundant_nodes.setter
    def redundant_nodes(self, value: pulumi.Input[int]):
        pulumi.set(self, "redundant_nodes", value)

    @property
    @pulumi.getter
    def compression_algorithm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "compression_algorithm")

    @compression_algorithm.setter
    def compression_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compression_algorithm", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encryption_algorithm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_algorithm")

    @encryption_algorithm.setter
    def encryption_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_algorithm", value)


@pulumi.input_type
class VMInputArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[int],
                 flist: pulumi.Input[str],
                 memory: pulumi.Input[int],
                 name: pulumi.Input[str],
                 network_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 entrypoint: Optional[pulumi.Input[str]] = None,
                 env_vars: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 flist_checksum: Optional[pulumi.Input[str]] = None,
                 gpus: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MountArgs']]]] = None,
                 planetary: Optional[pulumi.Input[bool]] = None,
                 public_ip: Optional[pulumi.Input[bool]] = None,
                 public_ip6: Optional[pulumi.Input[bool]] = None,
                 rootfs_size: Optional[pulumi.Input[int]] = None,
                 zlogs: Optional[pulumi.Input[Sequence[pulumi.Input['ZlogArgs']]]] = None):
        VMInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            flist=flist,
            memory=memory,
            name=name,
            network_name=network_name,
            description=description,
            entrypoint=entrypoint,
            env_vars=env_vars,
            flist_checksum=flist_checksum,
            gpus=gpus,
            mounts=mounts,
            planetary=planetary,
            public_ip=public_ip,
            public_ip6=public_ip6,
            rootfs_size=rootfs_size,
            zlogs=zlogs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: Optional[pulumi.Input[int]] = None,
             flist: Optional[pulumi.Input[str]] = None,
             memory: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             network_name: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             entrypoint: Optional[pulumi.Input[str]] = None,
             env_vars: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             flist_checksum: Optional[pulumi.Input[str]] = None,
             gpus: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MountArgs']]]] = None,
             planetary: Optional[pulumi.Input[bool]] = None,
             public_ip: Optional[pulumi.Input[bool]] = None,
             public_ip6: Optional[pulumi.Input[bool]] = None,
             rootfs_size: Optional[pulumi.Input[int]] = None,
             zlogs: Optional[pulumi.Input[Sequence[pulumi.Input['ZlogArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if cpu is None:
            raise TypeError("Missing 'cpu' argument")
        if flist is None:
            raise TypeError("Missing 'flist' argument")
        if memory is None:
            raise TypeError("Missing 'memory' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if network_name is None:
            raise TypeError("Missing 'network_name' argument")

        _setter("cpu", cpu)
        _setter("flist", flist)
        _setter("memory", memory)
        _setter("name", name)
        _setter("network_name", network_name)
        if description is not None:
            _setter("description", description)
        if entrypoint is not None:
            _setter("entrypoint", entrypoint)
        if env_vars is not None:
            _setter("env_vars", env_vars)
        if flist_checksum is not None:
            _setter("flist_checksum", flist_checksum)
        if gpus is not None:
            _setter("gpus", gpus)
        if mounts is not None:
            _setter("mounts", mounts)
        if planetary is not None:
            _setter("planetary", planetary)
        if public_ip is not None:
            _setter("public_ip", public_ip)
        if public_ip6 is not None:
            _setter("public_ip6", public_ip6)
        if rootfs_size is not None:
            _setter("rootfs_size", rootfs_size)
        if zlogs is not None:
            _setter("zlogs", zlogs)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[int]:
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[int]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def flist(self) -> pulumi.Input[str]:
        return pulumi.get(self, "flist")

    @flist.setter
    def flist(self, value: pulumi.Input[str]):
        pulumi.set(self, "flist", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[int]:
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[int]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def network_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def entrypoint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "entrypoint")

    @entrypoint.setter
    def entrypoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entrypoint", value)

    @property
    @pulumi.getter
    def env_vars(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "env_vars")

    @env_vars.setter
    def env_vars(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "env_vars", value)

    @property
    @pulumi.getter
    def flist_checksum(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "flist_checksum")

    @flist_checksum.setter
    def flist_checksum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flist_checksum", value)

    @property
    @pulumi.getter
    def gpus(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "gpus")

    @gpus.setter
    def gpus(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "gpus", value)

    @property
    @pulumi.getter
    def mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MountArgs']]]]:
        return pulumi.get(self, "mounts")

    @mounts.setter
    def mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MountArgs']]]]):
        pulumi.set(self, "mounts", value)

    @property
    @pulumi.getter
    def planetary(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "planetary")

    @planetary.setter
    def planetary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "planetary", value)

    @property
    @pulumi.getter
    def public_ip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter
    def public_ip6(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_ip6")

    @public_ip6.setter
    def public_ip6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip6", value)

    @property
    @pulumi.getter
    def rootfs_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rootfs_size")

    @rootfs_size.setter
    def rootfs_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rootfs_size", value)

    @property
    @pulumi.getter
    def zlogs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZlogArgs']]]]:
        return pulumi.get(self, "zlogs")

    @zlogs.setter
    def zlogs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZlogArgs']]]]):
        pulumi.set(self, "zlogs", value)


@pulumi.input_type
class ZDBInputArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 size: pulumi.Input[int],
                 description: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 public: Optional[pulumi.Input[bool]] = None):
        ZDBInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            password=password,
            size=size,
            description=description,
            mode=mode,
            public=public,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             password: Optional[pulumi.Input[str]] = None,
             size: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             mode: Optional[pulumi.Input[str]] = None,
             public: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if password is None:
            raise TypeError("Missing 'password' argument")
        if size is None:
            raise TypeError("Missing 'size' argument")

        _setter("name", name)
        _setter("password", password)
        _setter("size", size)
        if description is not None:
            _setter("description", description)
        if mode is None:
            mode = (_utilities.get_env('') or 'user')
        if mode is not None:
            _setter("mode", mode)
        if public is not None:
            _setter("public", public)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def public(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public")

    @public.setter
    def public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public", value)


@pulumi.input_type
class ZlogArgs:
    def __init__(__self__, *,
                 output: pulumi.Input[str],
                 zmachine: pulumi.Input[str]):
        ZlogArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            output=output,
            zmachine=zmachine,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             output: Optional[pulumi.Input[str]] = None,
             zmachine: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if output is None:
            raise TypeError("Missing 'output' argument")
        if zmachine is None:
            raise TypeError("Missing 'zmachine' argument")

        _setter("output", output)
        _setter("zmachine", zmachine)

    @property
    @pulumi.getter
    def output(self) -> pulumi.Input[str]:
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: pulumi.Input[str]):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter
    def zmachine(self) -> pulumi.Input[str]:
        return pulumi.get(self, "zmachine")

    @zmachine.setter
    def zmachine(self, value: pulumi.Input[str]):
        pulumi.set(self, "zmachine", value)


