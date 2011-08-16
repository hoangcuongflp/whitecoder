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
web=array('B', stdin.read(1)).tostring()

if (len(argv)<2): pass
elif (argv[1]=='-e'):
	while (web!=''):
		for bit in bin(ord(web))[2:].zfill(8)[::-1]:
			stdout.write(whitebin[bit])
		web=array('B', stdin.read(1)).tostring()
	exit(0)
elif (argv[1]=='-d'):
	whitebin=dict([(c,b) for (b,c) in whitebin.iteritems()])
	while (web!=''):
		if (web in whitebin.keys()): byte+=whitebin[web]
		if (len(byte)==8): stdout.write(chr(int(byte[::-1], 2))); byte=""
		web=array('B', stdin.read(1)).tostring()
	exit(0)

print argv[0], "[OPTION]\n\t-e to encode\n\t-d to decode"
