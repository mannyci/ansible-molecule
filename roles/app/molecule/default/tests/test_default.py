"""Role testing files using testinfra."""

import pytest

def test_nginx_is_installed(host):
	nginx = host.package("nginx")
	assert nginx.is_installed

def test_ssh_running_and_enabled(host):
	nginx = host.service("nginx")
	assert nginx.is_running
	assert nginx.is_enabled

def test_listening_http(host):
    socket = host.socket('tcp://0.0.0.0:80')
    assert socket.is_listening

def test_endpoint(host):
    command = """curl http://localhost:80/management"""
    cmd = host.run(command)

    assert '200 OK' in cmd.stdout
