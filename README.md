# Path Obfuscator (UNC Obfuscator)
Obfuscates linux and windows UNCs

I created this script to create user-obfuscated, but machine readable paths. It works on all OS that take wildcard characters in the UNC.

Functions as a simple, not-nesissarily smart obfuscator for UNCs. It is / and \ agnostic, but stay consistent with your path. It does not (intentionally) escape characters.
There are two functions, remote and local UNCs.

Remote takes any path without validation and obfuscates it the best it can. It can take a few runs of this to have a properly formatted obfuscation, so try at your own risk. This mode has a possible chance to not work due to wildcards overextending the file name size. WIP

Remote example:
``` bash
$ python3 path_obfuscator.py 
$ Are you checking local path or remote path? (l/r): r
$ Enter a path: C:\windows\system32
$ Obfuscated path: C:\*i***w*\?ys?****
```

Local takes the path and checks it against your local filesystem. If the path is correct and has no issues checking, then it recursively compares your pathname to similar pathnames (ls'ing every folder) to try and obfuscate common letters, and reveal unique characters. It creates the same obfuscated file every time, if the file structure remains the same on the host OS. This mode should always have a "correct" obfuscated path, but always double-check.
Invalid folder structure will result in this mode failing. If you need to try a theoretical path, use the "Remote" type.

Local Example:
 ``` bash
$ python3 path_obfuscator.py 
$ Are you checking local path or remote path? (l/r): l
$ Enter a path: /home/jp/Desktop
$ Obfuscated path: /h?me/jp/*?k*p
```

Issues to fix:
* (L:) Path with single folder showing complete folder
* (L:) Windows paths tending to overobfuscate in extremely large folders (e.g. system32), machine unreadable.
* (R:) Foldername length overwriting
