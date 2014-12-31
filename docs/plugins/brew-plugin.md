# brew.py

**class**: ``brewClient``

**functions**: ``install``, ``multi_install``

## Example Usage

```py
#!=party

from party_plugins import brew

task def install_packages():
	client = brew.gitClient() # create new client

	client.install('python3') # installs python3
```
