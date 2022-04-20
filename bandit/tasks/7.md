<h1>Bandit 7</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored <strong>somewhere on the
server</strong> and has all of the following properties:</p>
<ul>
  <li>owned by user bandit7</li>
  <li>owned by group bandit6</li>
  <li>33 bytes in size</li>
</ul>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find, grep</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit7@bandit.labs.overthewire.org -p 2220
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

bandit7@bandit:~$ grep millionth data.txt
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

[bandit level 6](bandit/tasks/bandit6.md)
[bandit level 8](bandit/tasks/bandit8.md)
