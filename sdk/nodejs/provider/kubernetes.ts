// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class Kubernetes extends pulumi.CustomResource {
    /**
     * Get an existing Kubernetes resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Kubernetes {
        return new Kubernetes(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grid:provider:Kubernetes';

    /**
     * Returns true if the given object is an instance of Kubernetes.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Kubernetes {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Kubernetes.__pulumiType;
    }

    public readonly master!: pulumi.Output<outputs.provider.K8sNodeInput>;
    public /*out*/ readonly master_computed!: pulumi.Output<outputs.provider.K8sNodeComputed>;
    public readonly network_name!: pulumi.Output<string>;
    public /*out*/ readonly node_deployment_id!: pulumi.Output<{[key: string]: number}>;
    public /*out*/ readonly nodes_ip_range!: pulumi.Output<{[key: string]: string}>;
    public readonly solution_type!: pulumi.Output<string | undefined>;
    public readonly ssh_key!: pulumi.Output<string | undefined>;
    public readonly token!: pulumi.Output<string>;
    public readonly workers!: pulumi.Output<outputs.provider.K8sNodeInput[]>;
    public /*out*/ readonly workers_computed!: pulumi.Output<{[key: string]: outputs.provider.K8sNodeComputed}>;

    /**
     * Create a Kubernetes resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KubernetesArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.master === undefined) && !opts.urn) {
                throw new Error("Missing required property 'master'");
            }
            if ((!args || args.network_name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'network_name'");
            }
            if ((!args || args.token === undefined) && !opts.urn) {
                throw new Error("Missing required property 'token'");
            }
            if ((!args || args.workers === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workers'");
            }
            resourceInputs["master"] = args ? args.master : undefined;
            resourceInputs["network_name"] = args ? args.network_name : undefined;
            resourceInputs["solution_type"] = args ? args.solution_type : undefined;
            resourceInputs["ssh_key"] = args ? args.ssh_key : undefined;
            resourceInputs["token"] = args ? args.token : undefined;
            resourceInputs["workers"] = args ? args.workers : undefined;
            resourceInputs["master_computed"] = undefined /*out*/;
            resourceInputs["node_deployment_id"] = undefined /*out*/;
            resourceInputs["nodes_ip_range"] = undefined /*out*/;
            resourceInputs["workers_computed"] = undefined /*out*/;
        } else {
            resourceInputs["master"] = undefined /*out*/;
            resourceInputs["master_computed"] = undefined /*out*/;
            resourceInputs["network_name"] = undefined /*out*/;
            resourceInputs["node_deployment_id"] = undefined /*out*/;
            resourceInputs["nodes_ip_range"] = undefined /*out*/;
            resourceInputs["solution_type"] = undefined /*out*/;
            resourceInputs["ssh_key"] = undefined /*out*/;
            resourceInputs["token"] = undefined /*out*/;
            resourceInputs["workers"] = undefined /*out*/;
            resourceInputs["workers_computed"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Kubernetes.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Kubernetes resource.
 */
export interface KubernetesArgs {
    master: pulumi.Input<inputs.provider.K8sNodeInputArgs>;
    network_name: pulumi.Input<string>;
    solution_type?: pulumi.Input<string>;
    ssh_key?: pulumi.Input<string>;
    token: pulumi.Input<string>;
    workers: pulumi.Input<pulumi.Input<inputs.provider.K8sNodeInputArgs>[]>;
}
