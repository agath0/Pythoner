"""Given a sorted array of integers , return the two numbers
    such that they add up to a specific target. You may assume
    that each input would have exactly one solution , and you
    may not use the same element twice  

    Refer this vedio for explanation

    https://youtu.be/gCin6Qz-eJQ    """

A=[-2,1,2,4,7,11]
target=13

#Time complexity: O(n^2)
#space complexity: O(1)
def twoSum_bruteForce(A,target):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==target:
                print(A[i],A[j])
                return True
    return False

print(twoSum_bruteForce(A,target))



print()

#Time Complexity : O(n)
#Space complexity : O(n)

def twoSum_hashTable(A,target):
    ht=dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]],A[i])
            return True
        else: 
            ht[target-A[i]]=A[i]
    return False

print(twoSum_hashTable(A,target))


print()



#But space complexity is also linear in the previous
# case but we need to reduce it to become efficient

#Time Complexity:O(n)
#Space Complexity:O(1)


def twoSum(A,target):
    i=0
    j=len(A)-1
    while i<=j:
        if A[i]+A[j]==target:
            print(A[i],A[j])
            return True
        elif A[i]+A[j]<target:
            i+=1
        else: 
            j-=1
    return False

print(twoSum(A,target))


