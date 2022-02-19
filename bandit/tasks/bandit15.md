<html>
<h1>Bandit 15</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level can be retrieved by submitting the
password of the current level to <strong>port 30000 on localhost</strong>.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ssh, telnet, nc, openssl, s_client, nmap</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://www.youtube.com/watch?v=7_LPdttKXPc">How the Internet works in 5 minutes (YouTube)</a> (Not completely
accurate, but good enough for beginners)</li>
  <li><a href="http://computer.howstuffworks.com/web-server5.htm">IP Addresses</a></li>
  <li><a href="https://en.wikipedia.org/wiki/IP_address">IP Address on Wikipedia</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Localhost">Localhost on Wikipedia</a></li>
  <li><a href="http://computer.howstuffworks.com/web-server8.htm">Ports</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Port_(computer_networking)">Port (computer networking) on Wikipedia</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit14@bandit.labs.overthewire.org -p 2220
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

bandit14@bandit:~$ echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e | nc localhost 30000
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

<p style="text-align: left"><a href="bandit/tasks/bandit14.md">Level 14</a></p>
<p style="text-align: right"><a href="bandit/tasks/bandit16.md">Level 16</a></p>
</html>
