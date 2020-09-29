#Inheritance
#is the mechanism of creating a new class from an 
#existin class
#The new class is the extended and modeified version
#of the existing class
#It facilitates code reuse
#Base class(super class)(parent)
#Derived class(sub class)(child)

#Note:every class in python inherits from an classs caled
#object ,the class object is the base class for any class

#Note:you should only use inheritance when there is any
#natural relationship between classes unessary use of 
#inhertance can make the system incomprehensible and
#and can create unwanted dependenceies between classes
class Person:
    def __init__(self,name,age,address,phone):
        self.name=name
        self.age=age
        self.address=address
        self.phone=phone

    def greet(self):
        print('hello i am ',self.name)

    def is_adult(self):
        if self.age>18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address,self.phone)

class Employee(Person):
    pass


class Employee1(Person):
    def __init__(self,name,age,address,phone,salary,sex):
        Person.__init__(self,name,age,address,phone)
        self.salary=salary
        self.sex=sex

#Note :use of super() is preffered because use of base 
#class name can create confusion in multiple inheritance
class Employee2(Person):
    def __init__(self,name,age,address,phone,salary,sex):
        super().__init__(name,age,address,phone)
        self.salary=salary
        self.sex=sex


emp=Employee('jack',39,'adxmcyadf','13434134')
print(emp.name)
print(emp.age)
print(emp.address)
print(emp.phone)
emp.contact_details()
print(emp.is_adult())

print()

emp1=Employee1('jack',39,'adxmcyadf','13434134',400,'male')
print(emp1.name)
print(emp1.age)
print(emp1.salary)
print(emp1.sex)
emp1.contact_details()
print(emp1.is_adult())


print()
emp2=Employee2('dany',39,'adxmcyadf','13434134',400,'female')
print(emp2.name)
print(emp2.age)
print(emp2.salary)
print(emp2.sex)
emp2.contact_details()
print(emp2.is_adult())



print()
print(isinstance(emp,Employee))
print(isinstance(emp,Person))
print(issubclass(Employee,Person))
print()
print(issubclass(Employee,object))
print(issubclass(Person,object))




