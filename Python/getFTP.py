#!/usr/bin/python3

#Download's a file from FTP or using FTP

import pexpect

#open connection and login
child = pexpect.spawn("ftp ftp.redhat.com") #child is the "object" I created
child.expect("Name .*:")
child.sendline("ftp")
child.expect("Password:")
child.sendline("ftp")

#child.expect("Name (ftp.redhat.com:justincase):")is what you could use 
#NOTE:if you wanted this script to be universal like this one you replace 
#you use what is above,after Name, with child.expect("Name .*:")
#".*" this is regular expression and makes it so its more universal

#change directory and download file
child.expect("ftp>")
child.sendline("cd /pub/redhat/linux/enterprise/7Server/en/Ansible")
child.expect("ftp>")
child.sendline("get ansible-2.5.7-1.el7ae.src.rpm")

#logout
child.expect("ftp>")
child.sendline("quit")
