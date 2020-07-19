#!/usr/bin/python3

#Example of writing a file 


#open the file 
testfile = open("testfile.txt", "w")
#the "w" stands for Writing

#write to the file 
testfile.write("Always look on the bright side of life\n")
testfile.write("your mother was XXX and your father smells of elderberries\n")
#close the file 
testfile.close()
