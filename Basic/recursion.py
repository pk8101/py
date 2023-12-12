#merge sort using recursio0n
def merge(l1,l2,l3):
    i=0
    j=0
    k=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l3[k]=l1[i]
            i=i+1
            k=k+1
        else:
            l3[k]=l2[j]
            j=j+1
            k=k+1
    while i<len(l1):
        l3[k]=l1[i]
        i=i+1
        k=k+1
    while j<len(l2):
        l3[k]=l2[j]
        j=j+1
        k=k+1



def mergeSort(l):
    if len(l)==0 or len(l)==1:
        return 
    mid=len(l)//2
    a1=l[0:mid]
    a2=l[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,l)


a4=[98,3,4,1,7,9,2]
mergeSort(a4)
print(a4)