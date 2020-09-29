#Tuples are the same as lists are with the exception that the data once entered into the tuple cannot be changed no matter what. The only exception is when the data inside the tuple is mutable, only then the tuple data can be changed. 


#creating

my_tuple = (1, 2, 3) #create tuple
print(my_tuple) 


#accessing elements

my_tuple1 = (1, 2, 3, 'edureka') #access elements
for x in my_tuple1:
    print(x)
print(my_tuple1)
print(my_tuple1[0])
print(my_tuple1[:])
print(my_tuple1[3][4])


#appending elements

my_tuple2 = (1, 2, 3)
my_tuple2 = my_tuple2 + (4, 5, 6) #add elements
print(my_tuple2)


#other functions

my_tuple3 = (1, 2, 3, ['hindi', 'python'])
my_tuple3[3][0] = 'english'
print(my_tuple3)
print(my_tuple3.count(2))
print(my_tuple3.index(['english', 'python']))


