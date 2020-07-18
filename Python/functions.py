#!/usr/bin/python3

#Basic Function

def func1():
  print("something func-y")

#function that takes an argument
def addNums(val1,val2):
  print(val1+val2)
#function that returns a value
def cube(x):
  return x * x * x
#function with default value
def power(num, power=2):#power inside parenthesis is squared 
  result=1
  for i in range (power):
    result=result * num
  print(result)

#Call Functions 
#func1()
#print(func1())
#print(func1)

#addNums(5, 6)# positional arguments
#addNums(val2 = 11, val1 = 9)
#print(cube(5)) #value of the function that is being called

power(6,6)
power(6,2)
power(6)

#named arguments 
#the only condition is you must stay with one or the other 
#example is you would have to keep doing postitional or named after you start 
