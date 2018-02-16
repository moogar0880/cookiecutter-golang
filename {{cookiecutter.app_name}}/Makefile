BIN_NAME={{cookiecutter.app_name}}

VERSION=$(shell git describe --tags 2> /dev/null || echo '0.0.0')
GIT_COMMIT=$(shell git rev-parse HEAD)
GIT_DIRTY=$(shell test -n "`git status --porcelain`" && echo "+CHANGES" || true)
PRERELEASE=
IMAGE_NAME := "{{cookiecutter.docker_hub_username}}/{{cookiecutter.app_name}}"

# if we have untagged commits, mark this build as a pre-release
ifneq ($(strip $(GIT_DIRTY)),)
PRERELEASE=DEV
endif

.PHONY: all
all: clean test

.PHONY: help
help:
	@echo 'Management commands for {{cookiecutter.app_name}}:'
	@echo
	@echo 'Usage:'
	@echo '    make build           Compile the project.'
	@echo '    make vendor          runs {{cookiecutter.vendor_tool}} to fetch vendor dependencies.'
	{% if cookiecutter.use_docker == "y" %}@echo '    make build-alpine    Compile optimized for alpine linux.'
	@echo '    make package         Build final docker image with just the go binary inside'
	@echo '    make tag             Tag image created by package with latest, git commit and version'
	@echo '    make test            Run tests on a compiled project.'
	@echo '    make push            Push tagged images to registry'{% endif %}
	@echo '    make clean           Clean the directory tree.'
	@echo

.PHONY: binary
binary:
	@echo "building ${BIN_NAME} ${VERSION}"
	@echo "GOPATH=${GOPATH}"
	go build -ldflags "-X main.Version=${VERSION} -X main.GitCommit=${GIT_COMMIT}${GIT_DIRTY} -X main.VersionPrerelease=${PRERELEASE}" -o bin/${BIN_NAME}

.PHONY: clean
clean:
	@test ! -e bin/${BIN_NAME} || rm bin/${BIN_NAME} && go clean

.PHONY: test
test:
	go test ./...

{% if cookiecutter.vendor_tool == "glide" %}
.PHONY: vendor
vendor:
	glide install
{% elif cookiecutter.vendor_tool == "dep" %}
.PHONY: vendor
vendor:
	dep ensure
{% endif %}

{% if cookiecutter.use_docker == "y" %}
##############################################################################
# The following targets are used for packaging the {{cookiecutter.app_name}}
# binary into a docker container
##############################################################################

.PHONY: build-alpine
build-alpine:
	@echo "building ${BIN_NAME} ${VERSION}"
	@echo "GOPATH=${GOPATH}"
	go build -ldflags '-w -linkmode external -extldflags "-static" -X main.GitCommit=${GIT_COMMIT}${GIT_DIRTY} -X main.VersionPrerelease=VersionPrerelease=RC' -o bin/${BIN_NAME}

.PHONY: package
package:
	@echo "building image ${BIN_NAME} ${VERSION} $(GIT_COMMIT)"
	docker build --build-arg VERSION=${VERSION} --build-arg GIT_COMMIT=$(GIT_COMMIT) -t $(IMAGE_NAME):local .

.PHONY: tag
tag: 
	@echo "Tagging: latest ${VERSION} $(GIT_COMMIT)"
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):$(GIT_COMMIT)
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):${VERSION}
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):latest

.PHONY: push
push: tag
	@echo "Pushing docker image to registry: latest ${VERSION} $(GIT_COMMIT)"
	docker push $(IMAGE_NAME):$(GIT_COMMIT)
	docker push $(IMAGE_NAME):${VERSION}
	docker push $(IMAGE_NAME):latest
{% endif %}
