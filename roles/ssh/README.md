Role Name
=========

ssh

Requirements
------------

None


Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - app

License
-------

BSD

Author Information
------------------

Author

Tests
-----

Below are the tests that must pass

- openssh-server installed
- sshd service enabled
- Port x is open
- Root login disabled
- Only ssh keys authentication mechanism enabled
