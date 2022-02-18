<html>
<h1>Bandit 11</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the file <strong>data.txt</strong>,
which contains base64 encoded data</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://en.wikipedia.org/wiki/Base64">Base64 on Wikipedia</a></li>
</ul>


<h1>Solution</h1>
```
user@host:~$ ssh bandit10@bandit.labs.overthewire.org -p 2220
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

<div style="text-align: left"><a href="bandit10.md">Level 10</a></div>
<div style="text-align: right"><a href="bandit12.md">Level 12</a></div>
</html>
