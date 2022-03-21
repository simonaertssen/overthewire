<h1>Bandit 29</h1>

<h2 id="level-goal">Level Goal</h2>
<p>There is a git repository at <code class="language-plaintext highlighter-rouge">ssh://<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aecccfc0cac7da9c9683c9c7daeec2c1cdcfc2c6c1ddda">[email&#160;protected]</a>/home/bandit28-git/repo</code>. The password for the user <code class="language-plaintext highlighter-rouge">bandit28-git</code> is the same as for the user <code class="language-plaintext highlighter-rouge">bandit28</code>.</p>

<p>Clone the repository and find the password for the next level.</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>git</p>


<h1>Solution</h1>

```
user@host:~$ ssh bandit29@bandit.labs.overthewire.org -p 2220
bbc96594b4e001778eee9975372716b2

bandit29@bandit:~$ mkdir /tmp/tmp
bandit29@bandit:~$ cd /tmp/tmp
bandit29@bandit:/tmp/tmp$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit29/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password:
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (16/16), 1.43 KiB | 0 bytes/s, done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp$ cat repo/README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
bandit29@bandit:/tmp/tmp/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp/repo$ git checkout dev
Branch dev set up to track remote branch dev from origin.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp/repo$ git log -p -1
commit bc833286fca18a3948aec989f7025e23ffc16c07
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:52 2020 +0200

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..39b87a8 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials

 - username: bandit30
-- password: <no passwords in production!>
+- password: 5b90576bedb2cc04c86a9e924ce42faf
```

<a href="bandit28.md">Level 28</a>
<a href="bandit30.md">Level 30</a>
