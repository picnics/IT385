#!/usr/bin/python3

#Expect script using PXSSH

from pexpect import pxssh


#create session and login
s = pxssh.pxssh()
s.login("192.168.0.111", "justincase", "Password01")
print("ssh login successful")


#send uptime command 
s.sendline("uptime")
s.prompt()
print(s.before)


#logout
s.logout()
