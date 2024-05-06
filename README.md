# Ansible Molecule test example

This repo contains example of how Molecule can be used and incorporated into Ansible Development Lifecycle

## The why
Test techniques play an important role in development, and this is no different when we are talking about Infrastructure as Code (IaC).

Developers are always testing, and constant feedback is crucial to drive development. If it takes too long to get feedback on a change, steps might be too large, identifying te breaking changes becomes hard to spot.

Baby steps and fast feedback are the important parts in TDD (test-driven development).
## Molecule

This is an example for how Molecule can be used to test the state of the automation.

In this example we are using [Testinfra](https://testinfra.readthedocs.io/en/latest/) to test the automation.

> Ansible as verifier can also be used to test. Here is an example [blog post](https://www.ansible.com/blog/developing-and-testing-ansible-roles-with-molecule-and-podman-part-2) on how to use Ansible to verify within molecule.

# Requirements

- ansible >= 2.9
- pytest
- ansible-builder
- pytest-testinfra

## Roles

There are two example roles with example tasks. The roles have the test cases defined in their respective README.

- [app](roles/app/README.md)
- [ssh](roles/ssh/README.md)




