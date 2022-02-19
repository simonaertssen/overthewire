<html>
<h1>Bandit 3</h1>

<h2 id="level-goal">Level Goal</h2>
<p>The password for the next level is stored in a file called <strong>spaces
in this filename</strong> located in the home directory</p>

<h2 id="commands-you-may-need-to-solve-this-level">Commands you may need to solve this level</h2>
<p>ls, cd, cat, file, du, find</p>

<h2 id="helpful-reading-material">Helpful Reading Material</h2>
<ul>
  <li><a href="https://www.google.com/search?q=spaces+in+filename">Google Search for “spaces in filename”</a></li>
</ul>


<h1>Solution</h1>

```
user@host:~$ ssh bandit2@bandit.labs.overthewire.org -p 2220
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat < spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

<a href="bandit/tasks/bandit2.md">Level 2</a>
<a href="bandit/tasks/bandit4.md">Level 4</a>
</html>
