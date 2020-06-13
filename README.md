# Ansible role: Golang

![Molecule Test](https://github.com/crgwilson/ansible-role-golang/workflows/Molecule%20Test/badge.svg)

Install [Go](https://golang.org/) using tarballs from `https://dl.google.com/go`

## Variables

Different versions of Go can be installed using the `go_version` variable. All the other ones are pretty straight forward and won't need tweaking in most cases.

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
