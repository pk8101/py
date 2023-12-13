# sortquick sort using recursio0n
def findpivot(l,si1,ei1):
    pivotvalue=l[si1]
    c=0
    for i in range(si1,ei1+1):  #finding number of elements smaller than pivotvalue
        if l[i]<pivotvalue:
            c=c+1
    pivotindex=si1+c
    l[si1+c],l[si1]=l[si1],l[si1+c]
    i=si1
    j=ei1
    while i<j:  #comparing right side and left side of elements with pivot value
        if l[i]<pivotvalue:
            i=i+1
        elif l[j]>=pivotvalue:
            j=j-1
        else :
            l[i],l[j]=l[j],l[i]
            i=i+1
            j=j-1
        
    return pivotindex

def quickSort(a,si,ei):
    if si>=ei:
        return
    pivot=findpivot(a,si,ei)
    quickSort(a,si,pivot-1)
    quickSort(a,pivot+1,ei)


a4=[98,3,4,1,7,9,2]
quickSort(a4,0,len(a4)-1)
print(a4)