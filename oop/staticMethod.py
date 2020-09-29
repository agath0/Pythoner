#Static method
#this is a method that uses neither class vareiables
#nor instance variables
#It doesnot have any special first parameter,it 
#can have regular parameters
#When a static method is callled python doestnot sent the
#class object or the instance object as the first argument
#and this is why this methods can access neither the
#instance object state  or the class object state

#So when you have to create a helper or a utility method
#that contains some login related to the class turn it into
#  a static method  

class MyClass():

    a=5
    def __init__(self,x):
        self.x=x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

    @staticmethod
    def method3(m,n):
        print(m+n)

m=MyClass(999)

m.method2()
m.method1()
m.method3(5,2)

