<html>
<h1>Bandit 2</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in a file called <strong>-</strong>
located in the home directory</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://www.google.com/search?q=dashed+filename">Google Search for “dashed filename”</a></li>
  <li><a href="http://tldp.org/LDP/abs/html/special-chars.html">Advanced Bash-scripting Guide - Chapter 3 - Special Characters</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit1@bandit.labs.overthewire.org -p 2220
boJ9jbbUNNfktd78OOpsqOltutMc3MY1

bandit1@bandit:~$ ls -a
-  .  ..  .bash_logout  .bashrc  .profile
bandit1@bandit:~$ cat < -
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

<p style="text-align: left"><a href="bandit/tasks/bandit1.md">Level 1</a></p>
<p style="text-align: right"><a href="bandit/tasks/bandit3.md">Level 3</a></p>
</html>
