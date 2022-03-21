<h1>Bandit 30</h1>

<h2 id="level-goal">Level Goal</h2>
<p>There is a git repository at <code class="language-plaintext highlighter-rouge">ssh://<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e381828d878a97d1dace848a97a38f8c80828f8b8c9097">[email&#160;protected]</a>/home/bandit29-git/repo</code>. The password for the user <code class="language-plaintext highlighter-rouge">bandit29-git</code> is the same as for the user <code class="language-plaintext highlighter-rouge">bandit29</code>.</p>

<p>Clone the repository and find the password for the next level.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>git</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit30@bandit.labs.overthewire.org -p 2220
5b90576bedb2cc04c86a9e924ce42faf

bandit30@bandit:~$ mkdir /tmp/pmt/
bandit30@bandit:~$ cd /tmp/pmt/
bandit30@bandit:/tmp/pmt$ git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit30/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password:
remote: Counting objects: 4, done.
remote: Total 4 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/pmt$ cat repo/README.md
just an epmty file... muahaha
```

Damn.

```
bandit30@bandit:/tmp/pmt/repo$ git log
commit 3aefa229469b7ba1cc08203e5d8fa299354c496b
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:54 2020 +0200

    initial commit of README.md
bandit30@bandit:/tmp/pmt/repo$ git tag
secret
bandit30@bandit:/tmp/pmt/repo$ git show secret
47e603bb428404d265f59c42920d81e5
```

<a href="bandit29.md">Level 29</a>
<a href="bandit31.md">Level 31</a>
