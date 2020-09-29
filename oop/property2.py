class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.diagonal=(self.length*self.breadth+self.breadth)**.5
        #note if you change lengeth or breadth then outputs of
        #area and perimeter will change accordingly 
        #but diagonal in the same method definiton willnot change
        #So if you change the value of an instance variable
        # any instance varible that is computed from it will
        #not change but outputs of other methods implemented 
        #from it will not change
        #So one solution is to implement diagona as a method
        #but then we will not be able tot access it as an 
        #instance variable whnever we have to acces it we will
        #have to put parenthesis and will break the existing 
        #client code who have used diagonal as an instance 
        #varible
        #So the solutionn is  to  turn it into a property

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)



class RectangleProp():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    @property 
    def diagonal(self):
        return (self.length*self.breadth+self.breadth)**.5

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


r=Rectangle(3,5)
print(r.diagonal)
print(r.area())
print(r.perimeter())
print()
r.length=10
print(r.diagonal)#here diagonal will nod change according
               #to the change in length
print(r.area())
print(r.perimeter())


print()
print()
print()
rr=RectangleProp(3,5)
print(rr.diagonal)
print(rr.area())
print(rr.perimeter())
print()
rr.length=100
print(rr.diagonal)#here diagonal will  change according
               #to the change in length
print(rr.area())
print(rr.perimeter())
