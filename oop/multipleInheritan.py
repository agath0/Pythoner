#Multiople Inheritance
#here a class inherits from more that one class
#example:: x inherits from a, b and c


#class x(a,b,c):
#    pass

#Multiple inheritance get complicated a it goes in 
#deeper.And searching for attributes in base classes
#do not remain straight forward
#To resolve any sort of conflict while searching for
#attributes in base classes python ues a well defined
#algorithm

#Method Resolution Order(MRO)
#Order in which python searches for attributes in 
#base classes
#MRO gives a linearized path for the inheritance 
#structure
#Python computes an  MRO for every class in the hierarch
#MRO is computed using the C3 linearization algorithm
#Roughly it works in a left to right manner and it
#searches each class only once.
#Look for more in documentation
#To see MRO of a class
#classname.__mro__
#classname.mro()
#help(classname)
#instance.__clas__.__mro  

class Person:
    def greet(self):
        print('i am aperon')

class Teacher:
    def greet(self):
        print('i am a teacher')

class Student:
    def greet(self):
        print('i am a student')

class TeachingAssistant(Student,Teacher):
    def gree(self):
        print('i am a teaching assistant')

x=TeachingAssistant()
x.greet()
x.gree()
print(TeachingAssistant.__mro__)
print(TeachingAssistant.mro())
