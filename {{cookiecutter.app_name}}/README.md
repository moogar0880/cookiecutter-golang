# {{cookiecutter.app_name}}

{{cookiecutter.project_short_description}}

[![Go Report Card](https://goreportcard.com/badge/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}})](https://goreportcard.com/report/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}})
[![GoDoc](https://godoc.org/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}?status.svg)](https://godoc.org/{{cookiecutter.git_root}}/{{cookiecutter.github_username}}/{{cookiecutter.app_name}})

## Getting started

This project requires Go to be installed. On OS X with Homebrew you can just run `brew install go`.

Running it then should be as simple as:

```console
$ make
$ ./bin/{{cookiecutter.app_name}}
```

### Testing

``make test``
