#!/usr/bin/python3
# coding: utf-8

import os

AGENTFOLDERKEY = "agent-folder"
SITEFOLDERKEY = "site-folder"
SITENAME = "site-name"
AGENTIGNORE = [
	".git",
	".gitignore"
]

def isInAgentIgnore(conf, path):
	getRealPath = lambda x: os.path.realpath(conf[AGENTFOLDERKEY] + "/" + x)
	for ignore in AGENTIGNORE:
		i = getRealPath(ignore)
		if (os.path.isfile(i) and path == i) or (os.path.isdir(i) and path.startswith(i)):
			return True
	return False

def order_file(conf, verbose):
	tempName = "temp"
	with open(conf[SITENAME])
	for key, folders in {AGENTFOLDERKEY:conf[AGENTFOLDERKEY], SITEFOLDERKEY:conf[SITEFOLDERKEY]}.items():
		print("---{}---".format(key))
		for folder, subfolder, files in os.walk(folders):
			for afile in files:
				f = os.path.realpath(os.path.join(folder, afile))
				if (key == AGENTFOLDERKEY and not isInAgentIgnore(conf, f)) or key == SITEFOLDERKEY:
					print(f)
