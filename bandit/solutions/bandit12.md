ssh bandit12@bandit.labs.overthewire.org -p 2220
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
mkdir /tmp/temp/
cp data.txt /tmp/temp/temporary.txt
cat temporary.txt | xxd -r > data
file data
mv data data2.gz
gzip -d data2.gz
file data2
mv data2 data3.bz
bzip2 -d data3.bz
mv data4 data5.tar
tar -d data5.tar
tar -xf data5.tar
file data5
file data5.bin
mv data5.bin data6.tar
tar -xf data6.tar
file data6.bin
mv data6.bin data6.bz
bzip2 -d data6.bz
file data6
mv data6 data7.tar
tar -xf data7.tar
file data8.bin
mv data8.bin data8.gz
gzip -d data8.gz
file data8
cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
