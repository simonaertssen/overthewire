<h1>Bandit 4</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in a hidden file in the
<strong>inhere</strong> directory.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit3@bandit.labs.overthewire.org -p 2220
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls -la inhere/
total 12
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden
bandit3@bandit:~$ cat inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

<a href="bandit3.md">Level 3</a>             <a href="bandit5.md">Level 5</a>
