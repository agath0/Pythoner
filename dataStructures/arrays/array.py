import array
arr=array.array('i',[1,2,3])

print("new arrray is ",end=" ")
for i in range(0,3):
    print(arr[i],end=" ")

print("\r")

arr.append(4);

print("append",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")

arr.insert(2,5)

print("\r")

print("isert",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

print("\r")

print("pop",arr.pop(2));
print("pop",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")


print("\r")
arr.remove(1)#removes first occurence of 1
print("remove",end=" ")
for i in range(0,3):
    print(arr[i],end=" ")


print("\r")
print("index",arr.index(3))
print("index",arr.index(2))


print("array",arr)
arr1=arr
arr1.reverse()
print("reverse",arr1)


print("datatype" ,arr.typecode)
print("itemsize" ,arr.itemsize)
print("buffer_info",arr.buffer_info())



arr.append(9);
arr.append(9);
arr.append(9);
print("count",arr.count(9))

for i in range(0,6):
    print(arr[i],end=" ")

arr1=array.array('i',[11,12,13])
arr.extend(arr1)
for i in range(0,len(arr)):
    print(arr[i],end=" ")

print("\r")

listt=[111,222,333]
print("fromlist")
arr.fromlist(listt)
print(arr)
for i in range(0,len(arr)):
    print(arr[i],end=" ")

print("\r")
listt1=arr.tolist()
print("tolist")
print(listt1)
for i in range(0,len(listt1)):
    print(arr[i],end=" ")
