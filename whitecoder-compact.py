#! /usr/bin/env python

__script__  =  "whitecoder-compact"
__version__ =  "1.0"
__author__  =  "Mohammed 'AnxiousNut' A. Mustafa"
__email__   =  "<Anxious.Nut@Gmail.com>"
__license__ =  "Creative Commons BY-NC-SA"

from sys import *
from array import array

whitebin={'0': '\x20', '1': '\x09'}
byte=''
web=array('B', stdin.read()).tolist()

if (len(argv)<2): pass
elif (argv[1]=='-e'):
	for byte in web:
		for bit in bin(byte)[2:].zfill(8)[::-1]:
			 stdout.write(whitebin[bit])
	exit(0)
elif (argv[1]=='-d'):
	whitebin=dict([(c,b) for (b,c) in whitebin.iteritems()])
	for wbit in web:
		if (chr(wbit) in whitebin.keys()): byte+=whitebin[chr(wbit)]
		if (len(byte)==8): stdout.write(chr(int(byte[::-1], 2))); byte=""
	exit(0)

print argv[0], "[OPTION]\n\t-e to encode\n\t-d to decode"
