```
user@host:~$ ssh bandit20@bandit.labs.overthewire.org -p 2220
GbKksEFF4yrVs6il55v6gwY5aVje5f0j

bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ nmap localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2022-02-19 21:02 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00030s latency).
Not shown: 997 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
113/tcp   open  ident
30000/tcp open  ndmps

Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
bandit20@bandit:~$ ./suconnect 30000/tcp
getaddrinfo: Servname not supported for ai_socktype
bandit20@bandit:~$ ./suconnect 30000
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
^C
bandit20@bandit:~$ ./suconnect 113
^[[A^[[A^C
bandit20@bandit:~$ ./suconnect 22
Read: SSH-2.0-OpenSSH_7.4p1
ERROR: This doesn't match the current password!
```

Ok, so `suconnect` is listening for input!

```
bandit20@bandit:~$ echo GbKksEFF4yrVs6il55v6gwY5aVje5f0j | netcat -lp 1234 &
[1] 10689
bandit20@bandit:~$ jobs
[1]+  Running                 echo GbKksEFF4yrVs6il55v6gwY5aVje5f0j | netcat -lp 1234 &
bandit20@bandit:~$ ./suconnect 1234
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```
