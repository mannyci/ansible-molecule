"""Role testing files using testinfra."""

import pytest

def test_ssh_is_installed(host):
	ssh = host.package("openssh-server")
	assert ssh.is_installed

def test_ssh_running_and_enabled(host):
	ssh = host.service("sshd")
	assert ssh.is_running
	assert ssh.is_enabled

# Test that ssh config is present and has expected permissions
@pytest.mark.parametrize("filename,owner,group,mode", [
	("/etc/ssh/sshd_config", "root", "root", 0o600),
])

def ssh_config_perms(host, filename, owner, group, mode):
	target = host.file(filename)
	assert target.exists
	assert target.user == owner
	assert target.group == group
	assert target.mode == mode

def ssh_file_contains(host):
	target = host.file('/etc/ssh/sshd_config')
	assert target.contains() == "PasswordAuthentication no"
	assert target.contains() == "PermitRootLogin no"
