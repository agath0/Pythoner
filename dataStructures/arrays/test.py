import array
def oneByOne(aaa,d,n):
    for i in range(d):
        temp=aaa[0]
        for x in range(1,n):
            aaa[x-1]=aaa[x]
        aaa[n-1]=temp
    print(*aaa)



ar=array.array('i',[1,2,3,4,5,6])
print(*ar)
oneByOne(ar,2,6)
