<h1>Bandit 8</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the file <strong>data.txt</strong>
next to the word <strong>millionth</strong></p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd</p>

<h1>Solution</h1>

```
user@host:~$ ssh bandit8@bandit.labs.overthewire.org -p 2220
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

<a href="bandit7.md">Level 7</a>
<a href="bandit9.md">Level 9</a>
