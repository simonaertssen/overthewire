```
user@host:~$ ssh bandit15@bandit.labs.overthewire.org -p 2220
BfMYroe26WYalil77FoDi9qh59eK5xNr

bandit15@bandit:~$ openssl s_client -ign_eof -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEZOzuVDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjEwOTMwMDQ0NTU0WhcNMjIwOTMwMDQ0NTU0WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAM9En7CC
uPr6cVPATLAVhWMU1hggfIJEp5sZN9RPUbK0zKBv802yD54ObHYmIge6lqqkgXOz
2AuI4UfCG4iMb0UYUCA/wISwNqUQrjcja0OnqzCTRscXzzoIsHbC8lGFzMDRz3Jw
8nBD6/2jvFt1rnBtZ4ghibNn5rFHRi5EC+K/AgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAD7/moj14DUI6/D6imJ8pQlAy/8lZlsrbyRnqpzjWaATShDYr7k3
umdRg+36MciNFAglE7nGYZroTSDCm650D81+797owSXLPAdp1Q6JfQH5LOni2kbw
UHcO9hwQ+rJzEgIlfGOic7dC5lj8DBU5tugY87RZGKiZ2GG77WXas9Iz
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 481AD0864A1DD19C4ADFD7726B835BDBCCAA7476F1C2F0EF38572464ED061E96
    Session-ID-ctx:
    Master-Key: 73CAD707FA01C3D0905F8BAE2B63488504CAE51BEB191A5A801DE85DA05915753FC64FDD7568DE510152590ECC057051
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 8a eb e8 f5 31 15 46 ad-b2 a8 10 c1 51 b9 66 14   ....1.F.....Q.f.
    0010 - 71 5a 12 23 0c f9 75 4e-8d e2 68 0b d7 4f 00 8b   qZ.#..uN..h..O..
    0020 - ac 0e e5 da 78 d3 d8 88-4d d8 9b 2a b7 10 67 2c   ....x...M..*..g,
    0030 - 84 c6 d6 6b 6a e6 c1 fb-66 2f 10 28 25 12 de 2b   ...kj...f/.(%..+
    0040 - 66 c2 20 8a 81 77 17 39-c3 29 77 ef f7 de 00 23   f. ..w.9.)w....#
    0050 - a3 1e a8 fa c5 5c 38 3d-5e f8 b2 1a e2 9f 35 f2   .....\8=^.....5.
    0060 - 65 44 21 e5 fd 2f 3e 99-d4 fe 03 04 02 9d 3d 06   eD!../>.......=.
    0070 - a8 e9 69 a5 a8 d5 cb 9b-f9 45 f0 c8 fa b5 b0 e3   ..i......E......
    0080 - 57 48 51 d8 01 2d 17 0a-bb 35 c0 ac b3 cb 73 0e   WHQ..-...5....s.
    0090 - 33 9e 33 9c 1b 08 10 75-f9 0e 20 25 18 e6 39 98   3.3....u.. %..9.

    Start Time: 1645221829
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed=
```
