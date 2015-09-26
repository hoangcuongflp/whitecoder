There are 3 different whitecoder scripts on this project page. The all do the exact same job, but with difference in efficiency and speed.

## whitecoder.py ##

This is the main script, the one that handles everything. It provides help in a man-page look, explains what errors occur - if any, and provides itself for usability. This python script is written with the "divide and conquer" principle in mind, it's full of functions which one can import and use (check the module page for more information). However, from between all of the 3, it's not the fastest nor the most efficient one, it's the one in the middle.

## whitecoder-compact.py ##

This is the compact version of whitecoder.py, a total rewrite of the whitecoder script. The reason of this its creation was to get the most compact code that can do the same job. This is the fastest script, but not the most efficient one.

## whitecoder-compact-stream.py ##

This is almost identical to whitecoder-compact.py, except that it reads from a stream and processes it on the fly instead of storing read data in memory and then process it (which both of the scripts above do). This is the least fast script, but is the most efficient. This would be your solution if you're going to process a huge data. By huge I mean something that might populate your ram!