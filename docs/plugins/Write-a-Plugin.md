# Write a plugin

``party`` is very extensible and everyone can create plugins for it. This is a little example of how to write an simple plugin which allows users executing a python script directly (support is integrated, but its just an example).

**Required components:**

- [python3](https://python.org/downloads)
- [party](https://github.com/torwart/party/releases)
- [Sublime Text](https://sublimetext.com)

_you also can use any other text editor._

**Write the code:**

Fire up Sublime text editor (or whatever text editor you use) and paste this (commented source):

```py
#!/usr/bin/env python

import os
import sys

# create a new class yourClassName will be represent in the partyfile like gitClient or brewClient
class yourClassName():
	# create an function, don't forget @staticmethod, uhh.. scriptpath represents the path to the script
	@staticmethod
	def yourFunction(scriptpath):
		# os.system(...) is general for executing cl args
		os.system('python ' + scriptpath)
```

**Save it right:**

Now you'll need to save the script. The script needs to be called from any directory, which means it can imported into an ``partyfile``.

As you know, an ``party`` installation writes plugins into the ``site-packages`` of an python installation (can be found under ``site-packages/party_plugins``). Save it there and close your editor.

**Test it out:**

Now you'll can test your script by running this (fire up python command line):

```py
>>> from party_plugins import YOURSCRIPTNAME
>>> testvar = YOURSCRIPTNAME.yourClassName()
>>> testvar.yourFunction('/path/to/any/script.py')
```

if the script executes, everything has worked fine!
