#!/usr/bin/env python

# Copyright 2014 Jan Kowalewicz and contributors. All rights reserved.
# The source code is governed by an MIT X11-License which can be found
# in the root directory.

# This file is part of 'party'

import os
import sys

class gitClient():
	# clone(giturl): allows you to clone a repo into the current folder
	@staticmethod
	def clone_repo(giturl):
		os.system('git clone ' + giturl)

	# fclone(giturl, destpath): allows you to clone a repo into a specific local folder
	@staticmethod
	def fclone(giturl, destpath):
		os.system('git clone ' + giturl + ' ' + destpath)	

	# update_repo(repopath): performs git pull on an repo
	@staticmethod
	def update_repo(repopath):
		os.system('cd ' + repopath + ' && git pull')

	# init_submodules(): pulls down submodules for project
	@staticmethod
	def init_submodules():
		os.system('git submodule update --init')

	# repo_init_submodules(repopath): pulls down submodules for a repo
	@staticmethod
	def repo_init_submodules(repopath):
		os.system('cd ' + repopath + ' && git submodule update --init')

	def pack_zip():
		pass
		# TODO: work with git archive (zip)

	def pack_tar():
		pass
		# TODO: work with git archive (tar)