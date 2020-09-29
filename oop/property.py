class Product:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def display(self):
        print(self._x,self._y)

    def value(self):
        return self._x


    @property  #after adding this line value1 become property
    def value1(self):
        return self._x

    @value1.setter
    def value1(self,val):
        self._x=val
        #whenever we reference the attribute the reference
        #property is called
        #and when we assign value to the atttribute the
        #setter is called

    @value1.deleter
    def value1(self):
        print('value deleted')
        #this method well get executed when we try to delete it 

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,val):
        self._y=val


p=Product(12,24) 
p.display()
print(p.value())
print(p.value1)#since its a property we can access
                #it like we access the instance variable
                #there is no need for parenthesis
                #@property is a decorator
                #we can only reference this attribute
                #we cannot assign anything to it


p.value1=999
print(p.value1)
del Product.value1
try:
    print(p.value1)
except Exception as e:
    print("thata attribute is deleted")

print()
print(p.y)
p.y=1111
print(p.y)
