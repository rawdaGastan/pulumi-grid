GOPATH := $(shell go env GOPATH)


DIRS := . $(shell find tests examples -type d)
GARBAGE_PATTERNS := Pulumi.test.yaml state
GARBAGE := $(foreach DIR,$(DIRS),$(addprefix $(DIR)/,$(GARBAGE_PATTERNS)))

all: verifiers test

build:
	go build -o pulumi-resource-grid github.com/rawdaGastan/pulumi-provider-grid

test: 
	@echo "Running Tests"
	go test -v `go list ./... | grep -v tests`

integration:
	@echo "Running integration tests"
	go test -v ./tests

coverage: clean 
	@echo "Installing gopherbadger" && go get -u github.com/jpoles1/gopherbadger && go install github.com/jpoles1/gopherbadger
	mkdir coverage
	go test -v -vet=off ./... -coverprofile=coverage/coverage.out
	go tool cover -html=coverage/coverage.out -o coverage/coverage.html
	@${GOPATH}/bin/gopherbadger -png=false -md="README.md"
	rm coverage.out
	go mod tidy

clean:
	rm ./coverage -rf
	rm -f schema-grid.json
	rm -f pulumi-resource-grid
	rm -rf $(GARBAGE)

getverifiers:
	@echo "Installing staticcheck" && go get -u honnef.co/go/tools/cmd/staticcheck && go install honnef.co/go/tools/cmd/staticcheck
	@echo "Installing gocyclo" && go get -u github.com/fzipp/gocyclo/cmd/gocyclo && go install github.com/fzipp/gocyclo/cmd/gocyclo
	@echo "Installing deadcode" && go get -u github.com/remyoudompheng/go-misc/deadcode && go install github.com/remyoudompheng/go-misc/deadcode
	@echo "Installing misspell" && go get -u github.com/client9/misspell/cmd/misspell && go install github.com/client9/misspell/cmd/misspell
	@echo "Installing golangci-lint" && go install github.com/golangci/golangci-lint/cmd/golangci-lint@v1.50.1

verifiers: fmt lint cyclo deadcode spelling staticcheck

checks: verifiers

fmt:
	@echo "Running $@"
	@gofmt -d .

lint:
	@echo "Running $@"
	@${GOPATH}/bin/golangci-lint run

cyclo:
	@echo "Running $@"
	@${GOPATH}/bin/gocyclo -over 100 .

deadcode:
	@echo "Running $@"
	@${GOPATH}/bin/deadcode -test $(shell go list ./...) || true

spelling:
	@echo "Running $@"
	@${GOPATH}/bin/misspell -i monitord -error `find .`

staticcheck:
	@echo "Running $@"
	@${GOPATH}/bin/staticcheck -- ./...
