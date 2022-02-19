<html>
<h1>Bandit 1</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in a file called
<strong>readme</strong> located in the home directory. Use this password to log
into bandit1 using SSH. Whenever you find a password for a level,
use SSH (on port 2220) to log into that level and continue the game.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit0@bandit.labs.overthewire.org -p 2220
bandit0

bandit0@bandit:~$ head readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

<p style="text-align: left"><a href="bandit/tasks/bandit0.md">Level 0</a></p>
<p style="text-align: right"><a href="bandit/tasks/bandit2.md">Level 2</a></p>
</html>
