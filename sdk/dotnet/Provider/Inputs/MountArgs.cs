// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Grid.Provider.Inputs
{

    public sealed class MountArgs : global::Pulumi.ResourceArgs
    {
        [Input("disk_name", required: true)]
        public Input<string> Disk_name { get; set; } = null!;

        [Input("mount_point", required: true)]
        public Input<string> Mount_point { get; set; } = null!;

        public MountArgs()
        {
        }
        public static new MountArgs Empty => new MountArgs();
    }
}
