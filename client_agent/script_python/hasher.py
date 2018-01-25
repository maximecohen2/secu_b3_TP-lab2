#!/usr/bin/python3
# coding: utf-8

import hashlib
import argparse
import os

DEFAULTBLOCKSIZE = 4096

def parse_args():
	parser = argparse.ArgumentParser(description="Hash the Files",
		usage="%(prog)s <address> <infile> <outname> [options]")
	parser.add_argument("-b", "--blocksize", metavar="SIZE", help="change the blocksize (default: " + str(DEFAULTBLOCKSIZE) + ")",
		type=str, default=DEFAULTBLOCKSIZE)
	parser.add_argument("-s", "--send-state", help="send state of progress of the hash", action="store_true")
	parser.add_argument("address", help="set address for send status", type=str)
	parser.add_argument("infile", help="file to be hash", type=str)
	parser.add_argument("outname", help="outfile's name", type=str)
	return parser.parse_args()

def get_filetohash(infile):
	with open(infile, "r") as afile:
		for line in afile:
			line = line.replace("\n", "")
			print(line)
			if os.path.isfile(line):
				yield line

def hash_data(file, blocksize):
	hasher = hashlib.sha1()
	with open(file, 'rb') as afile:
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		return hasher.hexdigest()

def hasher(address, outname, infile, blocksize):
	with open(outname, "w") as out:
		for hfile in get_filetohash(infile):
			out.write("{};{}\n".format(hfile, hash_data(hfile, blocksize)))

def main():
	args = parse_args()
	hasher(args.address, args.outname, args.infile, args.blocksize)


if __name__ == '__main__':
	main()
