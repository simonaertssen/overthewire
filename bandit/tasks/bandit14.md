<html>
<h1>Bandit 14</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in
<strong>/etc/bandit_pass/bandit14 and can only be read by user
bandit14</strong>. For this level, you don’t get the next password, but you
get a private SSH key that can be used to log into the next level.
<strong>Note:</strong> <strong>localhost</strong> is a hostname that refers to the machine
you are working on</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ssh, telnet, nc, openssl, s_client, nmap</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://help.ubuntu.com/community/SSH/OpenSSH/Keys">SSH/OpenSSH/Keys</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit13@bandit.labs.overthewire.org -p 2220
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

bandit13@bandit:~$ ip r
default via 192.168.101.1 dev eth0 onlink
192.168.101.0/24 dev eth0 proto kernel scope link src 192.168.101.80
bandit13@bandit:~$ nmap -p22 192.168.101.*
Starting Nmap 7.40 ( https://nmap.org ) at 2022-02-18 22:43 CET
Nmap scan report for 192.168.101.80
Host is up (0.00017s latency).
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 256 IP addresses (1 host up) scanned in 36.80 seconds

bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ ssh bandit14@192.168.101.80 -i sshkey.private
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

Interesting how we can pass through machines like that. I guess I didn't have to `nmap` after all.

<p style="text-align: left"><a href="bandit/tasks/bandit13.md">Level 13</a></p>
<p style="text-align: right"><a href="bandit/tasks/bandit15.md">Level 15</a></p>
</html>
