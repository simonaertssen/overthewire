```
user@host:~$ ssh bandit25@bandit.labs.overthewire.org -p 2220
uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

So if we rescale our terminal, then not all text should be printed at once and we can interact using vim.

```
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
v
:e /etc/bandit_pass/bandit26
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
```
