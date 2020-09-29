
#Why we need this
#consider  a situation
#there may be cases where we want to create instance objects o
#type person from different types of data
#for example in the form of a string or a dictionary
#you may read this data from a file or something
#now you want to be able to create an instance of type person
#from a string or a dictionary
#Python does not support function overloading so there can be
#only one type of initializer
#We cannot have more than one definitions or init methods
#inside a class
#So to add this functionallity to the class we have to rely
#on class methods

#So class methods allow as to  create alternative initializers
#for our class and this are called as factory methods


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print('I am ',self.name,self.age, 'years old')

    @classmethod
    def from_str(cls,s):
        name,age=s.split(',')
        return cls(name,int(age))
    #cls here refers to the class object
    #and writing this will create a new Person instance object

    @classmethod
    def from_dict(cls,d):
        return cls(d['name'],d['age'])

p1=Person('John',20)
p2=Person('Jack',34)


s='Jim,23'

p3=Person.from_str(s)
p3.display()

d={'name':'anna','age':22}
p4=Person.from_dict(d)
p4.display()
