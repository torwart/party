# git.py

**class**: ``gitClient``

**functions**: ``clone_repo``, ``fclone``, ``update_repo``, ``init_submodules``, ``repo_init_submodules``

**ignored functions**: ``pack_zip``, ``pack_tar``

## Example Usage

```py
#!=party

from party_plugins import git

task def get_repo():
	client = git.gitClient() # create new client

	client.clone_repo('https://github.com/example/example.git') # clone repo
```
