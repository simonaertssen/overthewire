<h1>Bandit 9</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the file <strong>data.txt</strong>
and is the only line of text that occurs only once</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://ryanstutorials.net/linuxtutorial/piping.php">Piping and Redirection</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit9@bandit.labs.overthewire.org -p 2220
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

bandit9@bandit:~$ strings data.txt | grep '='
========== the*2i"4
=:G e
========== password
<I=zsGi
Z)========== is
A=|t&E
Zdb=
c^ LAh=3G
*SF=s
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
S=A.H&^
```

[bandit level 8](bandit/tasks/bandit8.md)
[bandit level 10](bandit/tasks/bandit10.md)
