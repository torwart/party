#!/usr/bin/env python

# Copyright 2014 Jan Kowalewicz and contributors. All rights reserved.
# The source code is governed by an MIT X11-License which can be found
# in the root directory.

# This file is part of 'party'

import os
import sys

# WARNING: This plugin works only on OSX!

class brewClient():
	# install(packname): installs a package onto the system
	@staticmethod
	def install(packname):
		os.system('brew install ' + packname)

	# multi_install(packs): installs multiple packages onto the system
	@staticmethod
	def multi_install(packs):
		os.system('brew install ' + packs)


# TODO: work on more options such as creating homebrew packages (@all: can anyone help? doesnt run a mac)