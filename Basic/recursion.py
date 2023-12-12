#binary search using recursio0n
#1.List must be sorted
#2.we need start and end element

def binarySearch(l,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if(l[mid]==x):
        return mid
    elif l[mid]>x:
        return binarySearch(l,x,si,mid)
    elif l[mid]<x:
        return binarySearch(l,x,mid+1,ei)
         
    


a=[1,2,3,4,5,6,7,78,99]
b=3
print(binarySearch(a,b,0,len(a)-1))