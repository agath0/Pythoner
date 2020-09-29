#Magic methods
#These methods begin and end with double underscore
#These are used when we define a class and we want the 
#instance objects of that class to respond to some python 
#syntax we need to define some special methods 
#called magic methode
#Its also called Dunder methods because of the double
#underscore added before and after the name
#__init__
#__add__
#__mul__
#__sub__
#__eq__
#__len__
#
#Its also called magic methode as they are run atuomatically
#by the interpretre when an instance object is used in a 
#particular syntax
#Are used to ovrload operators and built in methods
#By overloading an operator we tell that operator to behave
#differently depending on the type of its operand
#
#We have alread used this overloading operators when
#we used
#4+5    #add
#'he'+'ho' #concatenate
#2*3    #multiply
#'he'*3 #repeat


############LOOK DOCUMENTATION FOR ALL THE LIST OF
            #########AVAILABLE MAGIC METHODS

#A program to use addition multiplication and division
# with our fraction objects


class Fraction:
    def __init__(self,nr,dr,dr=1):
        self.nr=nr
        self.dr=dr
        if self.dr<0:
            self.nr*=-1
            self.dr*=-1
        s
