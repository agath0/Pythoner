#Rotation of algorithms can be implemented using
#different algorithms like:
#-one by one algorithm
#-juggling algorithm
#-reversal algorithm
#-back swap algorthm


def oneByOne(arr, d, n): 
    for i in range(d): 
        temp = arr[0] 
        for i in range(n-1): 
            arr[i] = arr[i + 1] 
        arr[n-1] = temp 


              
  
def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ") 
  
arr = [1, 2, 3, 4, 5, 6, 7] 
print(*arr)
oneByOne(arr, 2, 7) 
print(*arr)
arr = [1, 2, 3, 4, 5, 6, 7] 
print(*arr)
