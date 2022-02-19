<h1>Bandit 19</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in a file <strong>readme</strong> in
the homedirectory. Unfortunately, someone has modified <strong>.bashrc</strong>
to log you out when you log in with SSH.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ssh, ls, cat</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit18@bandit.labs.overthewire.org -p 2220
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

Damn. Can't login. Let's see whether we can use another shell than bash.

```
user@host:~$ ssh bandit17@bandit.labs.overthewire.org -p 2220
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

bandit17@bandit:~$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/screen
/usr/bin/tmux
/usr/bin/showtext
```

```
ssh bandit18@bandit.labs.overthewire.org -p 2220 -t "/bin/sh"
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
$ ls
readme
$ cat readme
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

<a href="bandit18.md">Level 18</a>
<a href="bandit20.md">Level 20</a>
