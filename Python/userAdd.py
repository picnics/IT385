#!/usr/bin/python3

#adding a user to vm's through pxssh
from pexpect import pxssh

#create session and login
s = pxssh.pxssh()
s.login('192.168.0.111', 'justincase', 'Password01')
print('ssh login successful')

#adding new user with password
s.sendline('sudo useradd edgoad')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo passwd RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
print('succussfully added new user with password')

#logout
s.logout()
