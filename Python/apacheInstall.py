#!/usr/bin/python3
#installing apache via ssh with pxssh

from pexpect import pxssh
#create session and login
s = pxssh.pxssh()
s.login('192.168.0.111', 'edgoad', 'RubberDuck!')
print('ssh login successful')


#send apache commands
s.sendline('sudo dnf install httpd -y')
s.prompt()
print('package installed successful')
s.sendline('sudo systemctl start httpd.service')
s.prompt()
print('start the http service')
s.sendline('sudo systemctl enable httpd.service')
s.prompt()
print('auto start http service at boot successful')
s.prompt()
print(s.before)

#logout
s.logout()

