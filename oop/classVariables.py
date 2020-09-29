#a variable that is assigned at the class level 
#that is outside any method
#is called class variable or class attribute
#Its shared by all the instances of a class
#The data of the class variable is stored in class objects
#while in data of individual instance variables are
#stored in individual instancee objects
class Person:
    specie='homo sapiens'
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.specie
        #note : when we access the class variable through an
        #instanc python first checks wheather the instance 
        #contain that variable else it class variable will
        #be assigned to the instance variable also
        Person.count+=1

    def display(self):
        print(f'{self.name} is {self.age} years old {Person.specie} local {self.specie}')

p1=Person('john',29)
p2=Person('ageath',39)


p1.display()
p2.display()
print(p1.specie)
print(p2.specie)
print(id(p1.specie))
print(id(p2.specie))
print(Person.count)#this counts the no.of instance objects created
p3=Person('jooly',39)
p4=Person('amnohar',39)
p3.specie='monkey'#here class variable is redifined in the
                #instance of the p3 object 
print(p3.specie)
print(p4.specie)
p3.display()
p4.display()
print(Person.count)#this counts the no.of instance objects created 
