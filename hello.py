'''
#Understanding the basics of Python programming language:
//////////////////////////////////////////////////////////////

#Understanding the print function in Python:

massege = "Hello, World!"
time = "2024-06-01 12:00:00"

print(massege +"\n" + "The current time is: " + time)

#NB: The "\n" is used to create a new line in the output.
#NB: The "+" operator is used to concatenate (combine) strings in Python.
////////////////////////////////////////////////////////////////

#Understanding the input function in Python:

name = input("Enter your name: ")

def greet(name):
    answer = print("Hello, " + name + "!")

    return answer

greet(name)
//////////////////////////////////////////////////////////////

#Unsderstanding the JSON module in Python:

import json

# a Python object (dict):
x = open("names.json").read()

# convert into JSON:
y = json.loads(x)

# the result is a JSON string:
print(y)
//////////////////////////////////////////////////////////////

#Understanding the If statements and their syntax in Python:

a = 33
b = 200

if a > b :
    print("a is greater than b")
elif a == b :
    print("a and b are equal")  
else :
    print("a is less than b")
//////////////////////////////////////////////////////////////
'''
