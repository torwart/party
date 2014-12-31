#!/usr/bin/env python

# Copyright 2014 Jan Kowalewicz and contributors. All rights reserved.
# The source code is governed by an MIT X11-License which can be found
# in the root directory.

# This file is part of 'party'

import os
import sys

# WARNING: This plugin works only on UNIX machines which are able to run
# apt-get!

class aptGetClient():
	# install(packname): installs an package onto the system
	@staticmethod
	def install(packname):
		os.system('apt-get install ' + packname)

	# rootinstall(packname): installs an package using root access
	@staticmethod
	def rootinstall(packname):
		os.system('sudo apt-get install ' + packname)

	# multi_install(packs): installs multiple packages directly
	@staticmethod
	def multi_install(packs):
		os.system('apt-get install ' + packname)

	# root_multi_install(packs): installs multiple packages using root access
	@staticmethod
	def root_multi_install(packs):
		os.system('sudo apt-get install ' + packs)