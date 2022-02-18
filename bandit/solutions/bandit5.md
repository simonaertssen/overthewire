```
user@host:~$ ssh bandit5@bandit.labs.overthewire.org -p 2220
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ ls inhere/
maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
bandit5@bandit:~$ find ./ -type f -size 1033c ! -executable
./inhere/maybehere07/.file2
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```
