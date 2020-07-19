#!/usr/bin/python3

#logs into a remote system and runs the hostname command 

import pexpect
def getHostName(ipaddr):
  #open connection and login 
  child = pexpect.spawn("ssh justincase@" + ipaddr)
  child.expect("justincase@.* password:")
  child.sendline("Password01")
  print("logged into system")

  #send hostname command 
  child.expect("\[justincase@.*\]\$")
  child.sendline("hostname")
  print("got hostname")

  #logout
  child.expect("\[justincase@.*\]\$")
  print(child.before) 
  child.sendline("exit")
  print("logged out")
getHostName("192.168.0.111")
