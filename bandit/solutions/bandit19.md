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
