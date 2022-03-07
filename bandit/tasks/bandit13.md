<h1>Bandit 13</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in the file <strong>data.txt</strong>,
which is a hexdump of a file that has been repeatedly compressed.
For this level it may be useful to create a directory under /tmp in
which you can work using mkdir. For example: mkdir /tmp/myname123.
Then copy the datafile using cp, and rename it using mv (read the
manpages!)</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir,
cp, mv, file</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://en.wikipedia.org/wiki/Hex_dump">Hex dump on Wikipedia</a></li>
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

<a href="bandit12.md">Level 12</a>
<a href="bandit14.md">Level 14</a>
