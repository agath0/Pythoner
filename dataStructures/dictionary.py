#Dictionaries are used to store key-value pairs. To understand better, think of a phone directory where hundreds and thousands of names and their corresponding numbers have been added. Now the constant values here are Name and the Phone Numbers which are called as the keys. And the various names and phone numbers are the values that have been fed to the keys. If you access the values of the keys, you will obtain all the names and phone numbers. So that is what a key-value pair is


#creating

my_dict = {} #empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)

#changing or adding key,value pairs

my_dict1 = {'First': 'Python', 'Second': 'Java'}
print(my_dict1)
my_dict1['Second'] = 'C++' #changing element
print(my_dict1)
my_dict1['Third'] = 'Ruby' #adding key-value pair
print(my_dict1)

#deleting key value pairs

my_dict2 = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict2.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict2)
b = my_dict2.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict2)
my_dict2.clear() #empty dictionary
print('n', my_dict2)


#accessing elements

my_dict3 = {'First': 'Python', 'Second': 'Java'}
print(my_dict3['First']) #access elements using keys
print(my_dict3.get('Second'))


#other functions

my_dict4 = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
print(my_dict4.keys()) #get keys
print(my_dict4.values()) #get values
print(my_dict4.items()) #get key-value pairs
print(my_dict4.get('First'))



