# Introduction #
Whitecoder.py can be imported as a python module and used in your own python script or project. This is a sort of a quick reference.

The source code is also documented, so if you need to remember anything while at the interpreter, you can use the help function to check the description.

```
help(whitecoder)```

# Terminology #
Here are some terminology used throughout the script.

  * pyBinary: python's representation form of binary (e.g. '0b100001')
  * byteStr: 8-bit binary as string (e.g. '00100001')
  * bitChar: either 0 or 1 in the as characters (e.g. '1')
  * wsByte: 8 whitespace encoded bits as string (e.g. '  \t    \t')

# Functions #

## Encoding ##

### getBytes(inp) ###
Function expects a single argument, either of type int or char. It returns the binary value of it as pyBinary.

### getGeneralBytes(pyBinary) ###
Function expects a single argument of type pyBinary. Returns it as byteStr.

### whitespaceBitEncode(bitChar) ###
Function expects a single argument of type bitChar. It return an encoded bit.

### whitespaceEncode(byteSrt) ###
Function expects a single argument of type byteStr. Returns and encoded byte.

## Decoding ##

### byteStrToInt(byteStr) ###
Function expects a single argument of type byteStr. Returns its value as int.

### whitespaceByteDecode(wsByte) ###
Function expects a single argument of type wsByte. Returns a byteStr.