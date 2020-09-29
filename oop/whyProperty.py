
class Person:
    def __init__(self,name,age):
        self.name=name
        if 20<age<80:
            self._age=age
        else:
            raise ValueError('Age must be between 29 and 80"')
            
    def display(self):
        print(self.name,self._age)

    def set_age(self,new_age):
        if 20<new_age<80:
            self._age=new_age
        else:
            raise ValueError('Age must be between 20 and 80"')

    def get_age(self):
        return self._age







class PersonProp:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    
    def display(self):
        print(self._name,self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        if 20<new_age<80:
            self._age=new_age
        else:
            raise ValueError('Age must be between 20 and 80"')
            

if __name__=='__main__':
    p=Person('Raj',39)
    p.display()
    p.set_age(26)
    p.display()
    print(p.get_age())
    p.set_age(44)
    print(p.get_age())
    p.display()
    p.display()
    p=Person('Raj',69)
    p.display()



    pp=PersonProp('agath',29)
    pp.display()
    print(pp.age)
    pp.age+=1
    print(pp.age)
