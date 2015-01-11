# get.py

**class**: ``downloadClient``

**functions**: ``curl``, ``wget``

## Example Usage

```py
#!=party

from party_plugins import apt

task def install_packages():
	client = get.downloadClient() # create new client

	client.wget('https://example.com/example.zip') # gets an ZIP from URL
```
