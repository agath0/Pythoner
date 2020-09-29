#Sets are a collection of unordered elements that are unique. Meaning that even if the data is repeated more than one time, it would be entered into the set only once. It resembles the sets that you have learnt in arithmetic. The operations also are the same as is with the arithmetic sets. 


#creating

my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)


#adding elements

my_set1 = {1, 2, 3}
my_set1.add(4) #add element to set
print(my_set1)


#Operations in sets

#The different operations on set such as union, intersection and so on are shown below.


my_set3 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set3.union(my_set_2), '----------', my_set3 | my_set_2)
print(my_set3.intersection(my_set_2), '----------', my_set3 & my_set_2)
print(my_set3.difference(my_set_2), '----------', my_set3 - my_set_2)
print(my_set3.symmetric_difference(my_set_2), '----------', my_set3 ^ my_set_2)
my_set3.clear()
print(my_set3)



