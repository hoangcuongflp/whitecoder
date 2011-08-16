#! /usr/bin/env python

__script__  =  "whitecoder"
__version__ =  "1.0"
__author__  =  "Mohammed 'AnxiousNut' A. Mustafa"
__email__   =  "<Anxious.Nut@Gmail.com>"
__license__ =  "Creative Commons BY-NC-SA"

import sys

whitespace={0: '\x20',
			1: '\x09'}

def argError(msg):
	'''Prints the given message along with another message that tells to use -h option, then exits with return value 1'''
	sys.stderr.write("Error: "+msg+".\n")
	sys.stdout.write("Try `"+sys.argv[0]+" -h` for help.\n")
	sys.exit(1)

def argParse():
	'''Parses the arguments, provides help, and returns which option was entered'''
	options={'-e': ("encode", "Encodes data."),
			 '-d': ("decode", "Decodes data."),
			 '-v': ("version", "Displays the version"),
			 '-h': ("help", "Displays this message.")} 

	if (len(sys.argv)>2):
		argError("Too many arguments")
	elif (len(sys.argv)==1):
		argError("No arguments")

	if (len(sys.argv[1])!=2 or sys.argv[1][0]!='-' or sys.argv[1] not in options.keys()):
		argError("Invalid argument")

	if (sys.argv[1]=='-v'):
		sys.stdout.write(__script__+' v'+__version__)
		return 0
	elif (sys.argv[1]=='-h'):
		sys.stdout.write("NAME:\n\t"+__script__+" - A whitespace encoder/decoder script\n\n")
		sys.stdout.write("SYNOPSIS:\n\t"+__script__+" [OPTION]\n\n")
		sys.stdout.write("DESCRIPTION:\n\n\t"+"Encodes and decodes input steam.\n\n")
		for key in options.keys():
			sys.stdout.write("\t"+key+"\n\t\t"+options[key][1]+"\n")
		sys.stdout.write("\n");
		sys.stdout.write("VERSION:\n\t"+__version__+"\n\n")
		sys.stdout.write("AUTHOR:\n\t"+__author__+__email__+"\n\n")
		sys.stdout.write("LICENSE:\n\t"+__license__+"\n\n")
		return 0

	else:
		return sys.argv[1][1]

def getBytes(inp):
	'''changes char/int input into python binary'''
	if (type(inp)==str):
		if (len(inp)!=1):
			return 0
		else:
			out=bin(ord(inp))
	elif (type(inp)==int):
		if (len(str(inp))!=1):
			return 0
		else:
			out=bin(inp)
	else:
		return 0
	return out

def getGeneralBytes(pyBinary):
	'''changes python binary into general 8-bits string'''
	if (type(pyBinary)!=str or pyBinary[:2]!='0b'):
		return 0
	else:
		out=pyBinary[2:].zfill(8)
	return out

def whitespaceBitEncode(bitChar):
	'''encodes a single bitChar'''
	if (bitChar=='0'):
		return whitespace[0]
	else:
		return whitespace[1]

def whitespaceEncode(byteSrt):
	'''encodes a byteSrt'''
	out=""
	for digit in byteSrt[::-1]:
		out+=whitespaceBitEncode(digit)
	return out

def byteStrToInt(byteStr):
	'''changes byteStr to int''' 
	out=int('0b'+str(byteStr), 2)
	return out

def whitespaceByteDecode(wsByte):
	'''decodes a single encoded whitespace byte (8-whitespaces)'''
	out=""
	for space in wsByte[::-1]:
		if (space==whitespace[0]):
			out+='0'
		elif (space==whitespace[1]):
			out+='1'
	return chr(byteStrToInt(out))

def main():
	'''launches whitecoder script'''
	status=argParse()
	if (not status):
		return 0
	else:
		try:
			inp=sys.stdin.read()
		except:
			sys.stderr.write("Error: Input stream got broken.")
			sys.exit(1)

		if (status=='e'):
			for char in inp:
				binstr=getGeneralBytes(getBytes(char))
				if (binstr!=0):
					sys.stdout.write(whitespaceEncode(binstr))
				else:
					sys.stderr.write("Error: Could not encode '"+char+"'. Please contact the author.\n")
					sys.exit(1)
		elif (status=='d'):
			cursor=0
			length=len(inp)
			byte=""
			
			while (cursor<length):
				if (inp[cursor] in whitespace.values()):
					byte+=inp[cursor]
				
				cursor+=1
				
				if (len(byte)==8):
					sys.stdout.write(whitespaceByteDecode(byte))
					byte=""
				elif (len(byte)!=8 and cursor==length):
					sys.stderr.write("Error: Invalid Input.\n")
					sys.exit(1)

	return 0

if (__name__=="__main__"):
	main()
