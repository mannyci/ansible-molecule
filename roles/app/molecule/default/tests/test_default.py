"""Role testing files using testinfra."""

import pytest

def test_nginx_is_installed(host):
	nginx = host.package("nginx")
	assert nginx.is_installed

def test_ssh_running_and_enabled(host):
	nginx = host.service("nginx")
	assert nginx.is_running
	assert nginx.is_enabled
