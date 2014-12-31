#!/usr/bin/env python

# plugin tests

import os
import sys
sys.path.insert(0, '../plugins')

import git
import brew
import apt
# if you want to test using installed party and without let
# the plugins do their operations, please view plugin_tests2

# testing the git client
def test_git():
	client = git.gitClient()

	client.clone_repo("https://github.com/octocat/Hello-World.git")
	client.update_repo('Hello-World')

	# TODO: more tests

# testing the homebrew client
# NOTE: THIS ONLY WORKS ON OSX WITH INSTALLED HOMEBREW!
def test_brew():
	client = brew.brewClient()

	client.install("python3")
	client.multi_install("python3 pyqt5")

# testing the apt-get client
# NOTE: ONLY WORKS ON UNIX MACHINES WHO SUPPORTS APT
def test_apt():
	client = apt.aptGetClient()

	client.install("python3")
	client.rootinstall("python3 pyqt5")

if __name__ == '__main__':
	test_git()
	# on OSX you can enable this:
	#	test_brew()
	# on UNIX (machines) you can enable this:
	#	test_apt()
	# I run a Windows, so I am sorry for that.