#Lists are used to store data of different data types in a sequential manner. There are addresses assigned to every element of the list, which is called as Index. The index value starts from 0 and goes on until the last element called the positive index. There is also negative indexing which starts from -1 enabling you to access elements from the last to first. 

#Arrays vs. Lists

#Arrays and lists are the same structure with one difference. Lists allow heterogeneous data element storage whereas Arrays allow only homogenous elements to be stored within them.

my_list = [] #create empty list
print(my_list)
my_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(my_list)

#adding elements

my_list1 = [1, 2, 3]
print(my_list1)
my_list1.append([555, 12]) #add as a single element
print(my_list1)
my_list1.extend([234, 'more_example']) #add as different elements
print(my_list1)
my_list1.insert(1, 'insert_example') #add element i
print(my_list1)


#deleting elements

my_list2 = [1, 2, 3, 'example', 3.132, 10, 30]
del my_list2[5] #delete element at index 5
print(my_list2)
my_list2.remove('example') #remove element with value
print(my_list2)
a = my_list2.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', my_list2)
my_list2.clear() #empty the list
print(my_list2)


#accessing elements

my_list3 = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list3: #access elements one by one
    print(element)
print(my_list3) #access all elements
print(my_list3[3]) #access index 3 element
print(my_list3[0:2]) #access elements from 0 to 1 and exclude 2
print(my_list3[::-1]) #access elements in reverse


#other functions

my_list4 = [1, 2, 3, 10, 30, 10]
print(len(my_list4)) #find length of list
print(my_list4.index(10)) #find index of element that occurs first
print(my_list4.count(10)) #find count of the element
print(sorted(my_list4)) #print sorted list but not change original
my_list4.sort(reverse=True) #sort original list
print(my_list4)



