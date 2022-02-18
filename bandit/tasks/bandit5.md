<html>
<h1>Bandit 5</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the only human-readable
file in the <strong>inhere</strong> directory. Tip: if your terminal is messed
up, try the “reset” command.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>


<h1>Solution</h1>
```
user@host:~$ ssh bandit4@bandit.labs.overthewire.org -p 2220
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ ls inhere/
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~$ file */*
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
bandit4@bandit:~$ cat inhere/-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

<div style="text-align: left"><a href="bandit4.md">Level 4</a></div>
<div style="text-align: right"><a href="bandit6.md">Level 6</a></div>
</html>
