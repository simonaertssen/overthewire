<h1>Bandit 5</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the only human-readable
file in the <strong>inhere</strong> directory. Tip: if your terminal is messed
up, try the “reset” command.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>


<h1>Solution</h1>

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

<a href="bandit4.md">Level 4</a>
<a href="bandit6.md">Level 6</a>
