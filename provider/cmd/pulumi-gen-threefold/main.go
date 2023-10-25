// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"

	dotnetgen "github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	gogen "github.com/pulumi/pulumi/pkg/v3/codegen/go"
	nodejsgen "github.com/pulumi/pulumi/pkg/v3/codegen/nodejs"
	pythongen "github.com/pulumi/pulumi/pkg/v3/codegen/python"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"

	providerVersion "github.com/threefoldtech/pulumi-threefold/provider/pkg/version"
)

// TemplateDir is the path to the base directory for code generator templates.
// var TemplateDir string

// BaseDir is the path to the base pulumi-threefold directory.
var BaseDir string

// Language is the SDK language.
type Language string

const (
	DotNet Language = "dotnet"
	Go     Language = "go"
	NodeJS Language = "nodejs"
	Python Language = "python"

	argsNumber = 3
)

func main() {
	flag.Usage = func() {
		const usageFormat = "Usage: %s <language> <swagger-or-schema-file> <root-pulumi-xyz-dir>"
		_, err := fmt.Fprintf(flag.CommandLine.Output(), usageFormat, os.Args[0])
		contract.IgnoreError(err)
		flag.PrintDefaults()
	}

	var version string
	flag.StringVar(&version, "version", providerVersion.Version, "the provider version to record in the generated code")

	flag.Parse()
	args := flag.Args()
	if len(args) < argsNumber {
		flag.Usage()
		return
	}

	language, inputFile := Language(args[0]), args[1]

	BaseDir = args[2]
	// TemplateDir = filepath.Join(BaseDir, "provider", "pkg", "gen")
	outDir := filepath.Join(BaseDir, "sdk", string(language))

	switch language {
	case NodeJS:
		// templateDir := filepath.Join(TemplateDir, "nodejs-templates")
		writeNodeJSClient(readSchema(inputFile, version), outDir)
	case Python:
		// templateDir := filepath.Join(TemplateDir, "python-templates")
		writePythonClient(readSchema(inputFile, version), outDir)
	case DotNet:
		// templateDir := filepath.Join(TemplateDir, "dotnet-templates")
		writeDotnetClient(readSchema(inputFile, version), outDir)
	case Go:
		// templateDir := filepath.Join(TemplateDir, "_go-templates")
		writeGoClient(readSchema(inputFile, version), outDir)
	default:
		panic(fmt.Sprintf("Unrecognized language '%s'", language))
	}
}

func readSchema(schemaPath string, version string) *schema.Package {
	// Read in, decode, and import the schema.
	schemaBytes, err := os.ReadFile(schemaPath)
	if err != nil {
		panic(err)
	}

	var pkgSpec schema.PackageSpec
	if err = json.Unmarshal(schemaBytes, &pkgSpec); err != nil {
		panic(err)
	}
	pkgSpec.Version = version

	pkg, err := schema.ImportSpec(pkgSpec, nil)
	if err != nil {
		panic(err)
	}
	return pkg
}

func writeNodeJSClient(pkg *schema.Package, outDir string) {
	_, err := nodejsgen.LanguageResources(pkg)
	if err != nil {
		panic(err)
	}

	overlays := map[string][]byte{}
	files, err := nodejsgen.GeneratePackage("pulumigen", pkg, overlays)
	if err != nil {
		panic(err)
	}

	mustWriteFiles(outDir, files)
}

func writePythonClient(pkg *schema.Package, outDir string) {
	_, err := pythongen.LanguageResources("pulumigen", pkg)
	if err != nil {
		panic(err)
	}

	overlays := map[string][]byte{}
	files, err := pythongen.GeneratePackage("pulumigen", pkg, overlays)
	if err != nil {
		panic(err)
	}

	mustWriteFiles(outDir, files)
}

func writeDotnetClient(pkg *schema.Package, outDir string) {
	_, err := dotnetgen.LanguageResources("pulumigen", pkg)
	if err != nil {
		panic(err)
	}

	overlays := map[string][]byte{}
	files, err := dotnetgen.GeneratePackage("pulumigen", pkg, overlays)
	if err != nil {
		panic(err)
	}

	mustWriteFiles(outDir, files)
}

func writeGoClient(pkg *schema.Package, outDir string) {
	files, err := gogen.GeneratePackage("pulumigen", pkg)
	if err != nil {
		panic(err)
	}

	mustWriteFiles(outDir, files)
}

func mustWriteFiles(rootDir string, files map[string][]byte) {
	for filename, contents := range files {
		mustWriteFile(rootDir, filename, contents)
	}
}

func mustWriteFile(rootDir, filename string, contents []byte) {
	outPath := filepath.Join(rootDir, filename)

	const (
		dirPermissions  = 0o755
		filePermissions = 0o644
	)

	if err := os.MkdirAll(filepath.Dir(outPath), dirPermissions); err != nil {
		panic(err)
	}
	err := os.WriteFile(outPath, contents, filePermissions)
	if err != nil {
		panic(err)
	}
}
