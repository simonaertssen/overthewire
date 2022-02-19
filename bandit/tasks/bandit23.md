<h1>Bandit 23</h1>

<h2 id="level-goal">Level Goal</h2>
<p>A program is running automatically at regular intervals from
<strong>cron</strong>, the time-based job scheduler. Look in <strong>/etc/cron.d/</strong> for
the configuration and see what command is being executed.</p>

<p><strong>NOTE:</strong> Looking at shell scripts written by other people is a
very useful skill. The script for this level is intentionally made
easy to read. If you are having problems understanding what it does,
try executing it to see the debug information it prints.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>cron, crontab, crontab(5) (use “man 5 crontab” to access this)</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit22@bandit.labs.overthewire.org -p 2220
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

bandit22@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ /usr/bin/cronjob_bandit23.sh
Copying passwordfile /etc/bandit_pass/bandit22 to /tmp/8169b67bd894ddbb4412f91573b38db3
bandit22@bandit:~$ cat /tmp/8169b67bd894ddbb4412f91573b38db3
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

<a href="bandit22.md">Level 22</a>             <a href="bandit24.md">Level 24</a>
