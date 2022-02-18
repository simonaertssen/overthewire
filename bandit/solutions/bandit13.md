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
