```
user@host:~$ ssh bandit10@bandit.labs.overthewire.org -p 2220
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```
