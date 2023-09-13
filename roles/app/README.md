Role Name
=========

app

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

- Nginx installed
- Nginx service enabled
- Port x is open
- localhost/example/endpoint returns 200
- localhost/api/endpoint returns `{ ping: pong }`
