#!/usr/bin/python3

#installing mySQL on fedora through pxssh

from pexpect import pxssh
s = pxssh.pxssh()
s.login('192.168.0.121', 'justincase', 'Password01')
print('ssh login successfull')


#adding the MySql repository
s.sendline('sudo dnf install https://repo.mysql.com//mysql80-community-release-fc31-1.noarch.rpm')
s.prompt()
print('adding repository successful')

#install MySql on fedora linux
s.sendline('sudo dnf install mysql-community-server')
s.prompt()
print('Installing mysql on fedora successful')

#start mySql service and enable at login
s.sendline('sudo system start mysqld')
s.prompt()
s.sendline('sudo systemctl enable mysqld')

#logout
s.logout
