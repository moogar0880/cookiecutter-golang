# Build Stage
FROM {{cookiecutter.docker_build_image}} AS build-stage

WORKDIR /go/src/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
COPY . /go/src/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
RUN apk add --update --no-cache \
    gcc \
    git \
    make \
    musl-dev \
    && make binary/alpine

COPY . /go/src/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
WORKDIR /gopath/src/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}

RUN make binary/alpine

# essentials stage
FROM alpine:latest as alpine
RUN apk --no-cache add tzdata zip ca-certificates
WORKDIR /usr/share/zoneinfo
# -0 means no compression.  Needed because go's tz loader doesn't handle compressed data.
RUN zip -r -0 /zoneinfo.zip .

# production image stage
FROM scratch
COPY --from=build-stage /go/src/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/bin /bin

ENV ZONEINFO /zoneinfo.zip
COPY --from=alpine /zoneinfo.zip /

COPY --from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["/bin/{{cookiecutter.app_name}}"]
