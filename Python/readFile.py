#!/usr/bin/python3
#script to read a file 


#easy read of file 
testfile = open("testfile.txt", "r")
print(testfile.read(12))
testfile.close()


#read file line by line 
testfile = open("testfile.txt", "r")
for line in testfile:
  if line.startswith("A"):
    print(line)
testfile.close()


#read file using "WITH" statements 
with open("testfile.txt", "r") as testfile:
  print(testfile.read())

