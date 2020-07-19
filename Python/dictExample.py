#!/usr/bin/python3

#create disctionary object
#NOTE: we use curly braces when creating these

eng2esp = {"one":"uno", "two":"dos", "three":"tres"   }#english2spanish,one i#s the key and uno is value


print(eng2esp)

#view elements
print(eng2esp["one"])
print(eng2esp["three"])
#how to add and remove items from dictonary
eng2esp.update({"four":"quatro", "five":"cinco"})
eng2esp.pop("two")
#"pop" removes items from the dictionary
print(eng2esp)

#show all keys and values 
print(eng2esp.keys())
print(eng2esp.values())
