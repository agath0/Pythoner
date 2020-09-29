#Polymorphism
#ablity of code to take different forms depending
#on the tpe with which its used


class Car:
    def start(self):
        print('car engine started')
    def move(self):
        print('car is moving')
    def stop(self):
        print('car break appplied')
class Clock:
    def start(self):
        print('clock engine started')
    def move(self):
        print('clock is moving')
    def stop(self):
        print('clock break appplied')
class Person:
    def start(self):
        print('person engine started')
    def move(self):
        print('person is moving')
    def stop(self):
        print('person break appplied')

car=Car()
clock=Clock()
person=Person()

def do_something(x):
    x.start()
    x.move()
    x.stop()

print(do_something(car))
print(do_something(clock))
print(do_something(person))

#so any object that supports these three operation start,
#move ,stop  can be sent to this do_something function
#And the behaviour of move,start ,stop depends upon 
#the type of the object that they are operating upon
#This is polymorphism
#the same code can take different forms


#other OOP languages will need the classes to be 
#derived from a common base class to exchibit
#the polymorphic behaviour
#In python polymorphism does not depend on inheritance 
#For polymorphism to occur you just need to defince
#different classes which have commonly named methods
#Pythons polymorhpism is based on duck typing
#"if it walks like a duck and quacks like a duck
# then it is  a duck"

#The behaviour shown by oveloaded operator is 
#also polymorphism
