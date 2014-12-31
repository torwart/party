# apt.py

**class**: ``aptGetClient``

**functions**: ``install``, ``rootinstall``, ``multi_install``, ``root_multi_install``

## Example Usage

```py
#!=party

from party_plugins import apt

task def install_packages():
	client = apt.aptGetClient() # create new client

	client.install('python3') # installs python3
```
