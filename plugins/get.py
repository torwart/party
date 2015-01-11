#!/usr/bin/env python

# Copyright 2014-2015 Jan Kowalewicz and contributors. All rights reserved.
# The source code is governed by an MIT X11-License which can be found
# in the root directory.

# This file is part of 'party'

import os
import sys

class downloadClient():
	# curl(url): gets a file/gets files over curl
	@staticmethod
	def curl(url):
		os.system('curl -sS ' + url)

	# wget(url): gets a file/gets file over wget
	@staticmethod
	def wget(url):
		os.system('wget ' + url)	