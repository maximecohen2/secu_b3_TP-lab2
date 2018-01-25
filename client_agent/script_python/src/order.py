#!/usr/bin/python3
# coding: utf-8

import os
from hasher import hasher

AGENTFOLDERKEY = "agent-folder"
SITEFOLDERKEY = "site-folder"
SITENAME = "site-name"
AGENTIGNORE = [
	".git",
	".gitignore"
]
BLOCKSIZE = 4096

def isInAgentIgnore(conf, path):
	getRealPath = lambda x: os.path.realpath(conf[AGENTFOLDERKEY] + "/" + x)
	for ignore in AGENTIGNORE:
		i = getRealPath(ignore)
		if (os.path.isfile(i) and path == i) or (os.path.isdir(i) and path.startswith(i)):
			return True
	return False

def order_files(conf, verbose):
	fileName = conf[SITENAME] + "_files.order"
	with open(fileName, "a") as fInput:
		for key, folders in {AGENTFOLDERKEY:conf[AGENTFOLDERKEY], SITEFOLDERKEY:conf[SITEFOLDERKEY]}.items():
			fInput.write("---{}---\n".format(key))
			for folder, subfolder, files in os.walk(folders):
				for afile in files:
					f = os.path.realpath(os.path.join(folder, afile))
					if (key == AGENTFOLDERKEY and not isInAgentIgnore(conf, f)) or key == SITEFOLDERKEY:
						fInput.write("{}\n".format(f))

def order_hash(conf, verbose):
	tempOutName = "temp"
	hasher(conf['address'], tempOutName, "portfolioB_files.order", BLOCKSIZE)
