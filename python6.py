"""
#
# Part: Python Function
#
"""

def myFunction():
    i = 1
    while i <= 3:
        print("Hello World 1", i)
        i+=1

myFunction()    #ctrl + Lmouse
myFunction()

# parameter
def myName(name):
    print("My name is " + name)
myName("Anucha")

def myFullName(first_name = "Unknown", last_name = "Prachumpan"):
    print("My name is " + first_name + " " + last_name)
myFullName("Anucha")
myFullName(last_name = "Prachumpan",first_name = "Anucha") #กรณีจะสลับ แต่มันฝืน

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ["apple", "banana", "coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))