#Class method is a method that is associated with 
#a classs itself not with any particular instance of the class
#NOTE:
#class methods can only work with  class variables
#The class method can also be invoked using an instance
#but it makes more sense to invoke it using the class name 


class MyClass():
    a=5
    def __init__(self,x):
        self._x=x

    def method1(self):
        print(self.x)
    
    @classmethod      #this is a function decorator
    def method2(cls):
        print(cls.a)


MyClass.method2()
