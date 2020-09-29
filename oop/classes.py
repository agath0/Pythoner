
from sys import getsizeof as gs

class Person1:
    pass  #an empty class will be created


class Person:
    def set_details(self):
        self.name='John'
        self.age=20
    def display(self):
        print("I am a person",self)
        #python uses self parameter to identify the instance
        #object that calls the method
        #All the method should have this parameter

    def greet(self):
        print("hello,how are you doing?",self)


class Person2:
    def set_details(self,name,age):
        self.name=name
        self.age=age
        #self.name and self.age are instance varibles of the 
        #the same object but the parameters name and age 
        #which are passedd into the function are local variables
    def display(self):
        print("I am a person",self.name)
        print("I am a person",self.name)
        #python uses self parameter to identify the instance
        #object that calls the method
        #All the method should have this parameter

    def greet(self):
        if self.age<80:
            print("hello,how are you doing?")
        else:
            print("hello,how do you do")
        self.display()
        self.display()
        self.display()
        #so here we are calling a method in the class
        #form other method in the class


p1=Person() #p1 will refer to an instance object p1 whose
            #type is person
p2=Person()

print()
print(id(Person))
print(type(Person))
print(gs(Person))
print()

p1.set_details()
p2.set_details()
#whenver an instance object calls this method 
#set_details it will get the instance variables 
#attached to it
#Instance variables are specific to an instance of the
#class eevry instance have its own copy of instance variables
#making changes to instance varibles of one istance object
#will not affect the instance variables of other instance 
#objects


p1.display()
p1.greet()

p2.display()
p2.greet()


print(id(p1))
print(id(p2))
print(type(p2))
print(type(p1))
print(gs(p2))
print(gs(p1))



print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)

p1.name='agath'

print(p1.name)
print(p2.name)

p3=Person2()
p4=Person2()
p3.set_details('bob',20)
p4.set_details('loolan',80)
print(p4.name)
print(p3.name)

p3.display()
p3.greet()
