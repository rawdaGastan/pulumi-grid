// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Threefold.Provider.Outputs
{

    [OutputType]
    public sealed class Zlog
    {
        public readonly string Output;
        public readonly string Zmachine;

        [OutputConstructor]
        private Zlog(
            string output,

            string zmachine)
        {
            Output = output;
            Zmachine = zmachine;
        }
    }
}
