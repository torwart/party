#!/usr/bin/env python

# plugin tests reloaded

import os
import sys

from party_plugins import git
from party_plugins import brew
from party_plugins import apt

def test_git():
	client = git.gitClient()

def test_brew():
	client = brew.brewClient()

def test_apt():
	client = apt.aptGetClient()

if __name__ == '__main__':
	test_git()
	test_brew()
	test_apt()