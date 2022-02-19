<h1>Bandit 18</h1>

<h2 id="level-goal">Level Goal</h2>
<p>There are 2 files in the homedirectory: <strong>passwords.old and
passwords.new</strong>. The password for the next level is in
<strong>passwords.new</strong> and is the only line that has been changed between
<strong>passwords.old and passwords.new</strong></p>

<p><strong>NOTE: if you have solved this level and see ‘Byebye!’ when trying
to log into bandit18, this is related to the next level, bandit19</strong></p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>cat, grep, ls, diff</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit17@bandit.labs.overthewire.org -p 2220
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

<a href="bandit17.md">Level 17</a>             <a href="bandit19.md">Level 19</a>
