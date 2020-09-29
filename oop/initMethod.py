
class PersonWithOutInit:
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
        #so here we are calling a method in the class
        #form other method in the class

class PersonWithInit:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sex=None
        #self.name and self.age are instance varibles of the 
        #the same object but the parameters name and age 
        #which are passedd into the function are local variables
    def display(self):
        print("I am a person",self.name)
        print("I am a person",self.age)
        print("I am a person",self.sex)
        #python uses self parameter to identify the instance
        #object that calls the method
        #All the method should have this parameter

    def greet(self):
        if self.age<80:
            print("hello,how are you doing?")
        else:
            print("hello,how do you do")
        self.display()
        #so here we are calling a method in the class
        #form other method in the class

    def change(self):
        self.sex='male'



ps=PersonWithOutInit()
ps.set_details('loolan',80)
ps.display()
ps.greet()

print()
print()
print()

p=PersonWithInit('loolan',80)
p.display()
p.greet()
print(p.sex)
p.change()
print(p.sex)

#So what happens when you use init method in class is that
#the process of setting variables is done automatically and
#you will not need to do this manual by calling other
#function like set_details
#Any arguments that you pass to the class are passed to the
#init method and will not need further set initiation
#---Initialization work is done automatically
#---you can create and initialize all your instance
#    variables in this method
#---you can also perform any othe initialization tasks
#---the first parameter to __init__ is always self
#---other parameters are used to give initial values to 
#   instance variables
#---there are other dunder(--  --)methode also having
#   special names
#--- __init__is the initializer method,its the first method
#   its the first method thats called on the newly created
#   instance object
#---you can have only one initializer method in a class
#   since there is no concept of python overloading in python
#---to construct an instance ,the __new__magic method is 
#   invoked

#NOTE:if you have worked on other OOP languages like java or
# cpp you might be thinking of constructor from the starting
# of this note though it look similar it would be technically
# incorrect to call it the constructor of the class in python
# because by the time this method is called the object is 
# already constructed

