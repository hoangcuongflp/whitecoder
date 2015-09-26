## Options ##

```
./whitecoder.py OPTION```

  * Encoding option: -e
  * Decoding option: -d

## I/O ##

### Input ###
You can use any type of data to be processed, let it be sound-tracks, images, documents, or even executables.

### Output ###
Whitespace encoded binary following <a href='http://sigh.asia/playground/whitespace/specification.html'>SIGTERMer's specification</a> must be entered. Other than that, it will not decode correctly.

## Examples ##

### Encoding ###
```
./whitecoder.py -e
Encode this```

In this case you have to insert the end-of-transmission character. Ctrl+D if using Linux; Ctrl+Z if using Windows. Once that is entered, you would get the output.

```
 echo "Encode this" | ./whitecoder.py -e```

This would output the result directly.

```
 cat FILE | ./whitecoder.py -e```

This would encode any type of file and output the result on the screen. In order to keep the whitespace encoding in a file, redirect the output:

```
 cat FILE | ./whitecoder.py -e > FILE.web```

### Decoding ###
```
 cat FILE.web | ./whitecoder.py -d```

This would output the content of the original file on screen. In case you wish to keep it in a file, redirect it into a file:

```
 cat FILE.web | ./whitecoder.py -d > FILE```

But in case you would like to paste a whitespace encoded data directly, you can access it directly:

```
./whitecoder.py -d```

When data is pasted, you will have to insert the end-of-transmission character. Ctrl+D if using Linux; Ctrl+Z if using Windows. Once that is entered, you would get the output.