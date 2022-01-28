# Bash CheatSh\*t

Bash is the command language used in most of the Linux distributions and macOS (up to Catalina version). In my opinion, it is of extreme importance to get fluent in Bash, as soon as you can. If you are a self-learner or if you don't have a pure computer science/telecomunications background (as me) you will struggle a lot when starting and you will spend most of the time searching on stack overflow how to do "basic" stuff. Be patient, experience is the key. 

The goal of this tutorial is not to teach Bash, but to summarize those commands that I've looked up tons of times. Also, I will add some common terminal keyboard shortcuts that I know.  When pasting the commands, all parts between \<these symbols\> must be substituted by your own info. 

## Managing files
* ``` rsync ```: transferring files from/to a remote server. Example:
``` rsync -avzP <source_localfile_or_localdir> <username>@<server.com>:<destination_path> ``` , where ```a``` specifies archive mode, ```v``` verbose, ```z``` stands for "compress file data during the transfer" and ```P``` forces to keep partially transferred files. The first argument is the source and the second the destination, and this command works in both directions as long as you have configured both ways the ssh keys.

## Editing files
* ``` sed ```: find and replace. Example:
``` sed -i 's/<pattern1>/<pattern2>/g' <file> ```. This command replaces all ocurrences of <pattern1> by <pattern2> in <file> and updates the file (```-i````).
