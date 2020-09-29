
from employee import Employee
from datetime import datetime

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
    
    @classmethod
    def from_employee(cls,emp):
        name=emp._first_name+' '+emp._last_name
        age=datetime.today().year-emp._birth_year
        return cls(name,age)

p1=Person('John',20)
p2=Person('Jack',34)


s='Jim,23'

p3=Person.from_str(s)
p3.display()

d={'name':'anna','age':22}
p4=Person.from_dict(d)
p4.display()


e=Employee('james','Smith',1990,5000)
p5=Person.from_employee(e)
p5.display()
