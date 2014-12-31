# ``party`` :tada:

> The python task runner

``party`` is an task runner written in python for python. It automates all the steps which the users need to do, like installing components, updating dependencies or getting the latest source. Also its very extensible and you can [create](https://github.com/torwart/party/blob/master/docs/plugins/Write-a-Plugin.md) and [install](https://torwart.github.io/party-registry) plugins. You can view the [documentation](https://github.com/torwart/party/blob/master/docs) for more informations.

## Installation

You'll need to install

- [python3.4.2](https://python.org/downloads)
- [git](https://git-scm.com)

first (_installer script on Windows supports only Python 3.4.x_).

#### Windows

Start the command prompt (or use Git Bash) and run the following:

    $ git clone https://github.com/torwart/party.git
    $ cd party/bin
    $ python install-win32

If you receive an ``INSTALLED SUCCESSFULLY AND COPIED PLUGINS!``, you can be 100% sure that ``party`` is installed correctly. **But dont't forget to add the ``bin`` directory to your PATH!**

_If you use an older version of Python you can follow the steps for Linux/OSX to manual install party!_

#### Linux/OSX

_Currently I am not able to run an Linux or OSX system and this is a manual way to install ``party`` (would be nice if anyone could write an installer script)_

1. Download the latest source of ``party``
2. Extract it to any location
3. Create an new folder in your [Python site packages folder](https://docs.python.org/2/install/#how-installation-works) with the name ``party_plugins``
4. Copy all files from the ``plugins`` folder into it
5. Add the ``bin`` directory to your **PATH**
6. _not required:_ on some systems you'll need to reboot

Now you can test if ``party`` was successfully installed. This can be done using the ``Python command line``, fire it up and run this:

```py
>>> from party_plugins import git
>>> client = git.gitClient()
```

If this return no errors, you can be sure that you've installed ``party`` on your system.

## Sample ``partyfile.py``

An ``partyfile`` is recognized by the ``party`` CLI tool and contains the tasks you'll want to automate.

This is an simple example which uses the Git plugin:

```py
#!=party

# you can also import everything using 'import *'
from party_plugins import git

# creating tasks need the 'task' before the 'def' keyword
task def example_task():
    client = git.gitClient()

    client.clone_repo('https://github.com/example/example.git')

# now we need to make it available to run the task
def runTasks():
	example_task() # runs the example_task() task
```

## Shipped plugins

These plugins are shipped with ``party``:

- [.git](https://github.com/torwart/party/blob/master/plugins/git.py): an easy to use git client for your partyfiles
- [.brew](https://github.com/torwart/party/blob/master/plugins/brew.py): an easy to use homebrew client for your partyfiles (**OSX only**)
- [.apt](https://github.com/torwart/party/blob/master/plugins/apt.py): an easy to use apt-get client for your partyfiles (**UNIX only**)

## Known Issues

**Windows**

- _starting party from command line doesn't works. msys and git bash recommended_

Feel free to report any issue you get [here](https://github.com/torwart/party/issues)

## License

``party`` is published under the terms of the [MIT License](https://github.com/torwart/party/blob/master/LICENSE).
