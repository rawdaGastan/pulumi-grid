// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Threefold.Provider.Inputs
{

    public sealed class DiskArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        public DiskArgs()
        {
        }
        public static new DiskArgs Empty => new DiskArgs();
    }
}
