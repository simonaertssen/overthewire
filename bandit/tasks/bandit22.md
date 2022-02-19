<h1>Bandit 22</h1>

<h2 id="level-goal">Level Goal</h2>
<p>A program is running automatically at regular intervals from
<strong>cron</strong>, the time-based job scheduler. Look in <strong>/etc/cron.d/</strong> for
the configuration and see what command is being executed.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>cron, crontab, crontab(5) (use “man 5 crontab” to access this)</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit21@bandit.labs.overthewire.org -p 2220
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

bandit21@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit23       .placeholder
cronjob_bandit17_root  cronjob_bandit24
cronjob_bandit22       cronjob_bandit25_root
bandit21@bandit:~$ ls /etc/cron.d/cronjob_bandit22
/etc/cron.d/cronjob_bandit22
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

<a href="bandit21.md">Level 21</a>             <a href="bandit23.md">Level 23</a>
