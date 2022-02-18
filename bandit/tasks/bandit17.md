<html>
<h1>Bandit 17</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The credentials for the next level can be retrieved by submitting the
password of the current level to <strong>a port on localhost in the range
31000 to 32000</strong>. First find out which of these ports have a server
listening on them. Then find out which of those speak SSL and which
don’t. There is only 1 server that will give the next credentials, the
others will simply send back to you whatever you send to it.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ssh, telnet, nc, openssl, s_client, nmap</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://en.wikipedia.org/wiki/Port_scanner">Port scanner on Wikipedia</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit16@bandit.labs.overthewire.org -p 2220
cluFn7wTiGryunymYOu4RcffSxQluehd

```

<div style="text-align: left"><a href="./bandit16.md">Level 16</a></div>
<div style="text-align: right"><a href="./bandit18.md">Level 18</a></div>
</html>
