class Product:

    def __init__(self):
        self.data1=10
        self._data2=10
        self.__data3=20

    def methodA(self):
        pass
    def __methodB(self):
        pass

p=Product()

print(p.data1)

print(p._data2)#so this can directly give the output


#print(p.data3)#will not get output
print(dir(p))
print(p._Product__data3)#_Product__data3 is a name 
                        #available from dir(p)

