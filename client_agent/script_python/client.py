#!/usr/bin/python3
# coding: utf-8

import argparse
import os

from src.order import order_file

DEFAULTDATACONF = ["address", "site-folder", "agent-folder"]

DEFAULTCONFPATH = "./conf"
#ORDERS = {
#	FILES :
#}

def parse_args():
	parser = argparse.ArgumentParser(description="Client Agent",
		usage="%(prog)s <order>")
	parser.add_argument("order", help="set the order", type=str)
	parser.add_argument("-v", "--verbose", help="display more", action="store_true")
	args = parser.parse_args()
	if args.verbose:
		print("args: " + str(args))
	return args

def check_conf(conf):
	for data in conf:
		if data not in DEFAULTDATACONF:
			print("ERROR: missed \"{}\" in conf".format(folder))
	for folder in ["site-folder", "agent-folder"]:
		if not os.path.isdir(conf[folder]):
			print("ERROR: can't find folder \"{}\"".format(conf[folder]))
	if "address" not in conf:
		print("ERROR: can't find folder \"{}\"".format(conf[folder]))

def parse_conf(verbose):
	conf = {}
	confFile = os.path.realpath(os.path.dirname(os.path.abspath(__file__)) + "/" + DEFAULTCONFPATH)
	with open(confFile, "r") as cfile:
		for line in cfile:
			line = line.replace(" ", "")
			line = line.replace("\"", "")
			line = line.replace("\t", "")
			line = line.replace("\n", "")
			tab = line.split(":")
			conf[tab[0]] = tab[1]
	if verbose:
		print("conf: " + str(conf))
	return conf


def main():
	args = parse_args()
	conf = parse_conf(args.verbose)
	order_file(conf, args.verbose)

if __name__ == '__main__':
	main()
