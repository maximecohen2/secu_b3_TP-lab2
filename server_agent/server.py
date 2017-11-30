#!/usr/bin/python3
# coding: utf-8

import hashlib

def parse_args():
	parser = argparse.ArgumentParser(description="Run the server")
	#parser.add_argument("param", help="aide", type=str)
	return (parser.parse_args())

def main():
	args = parse_args()
	

if __name__ == '__main__':
	main()
