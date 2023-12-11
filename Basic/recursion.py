#find first index in array using recursio0n

def firstIndex(l,s,b):
    if(len(l)==s):
        return -1
    elif l[s]==b:
        return s
    else:
        return firstIndex(l,s+1,b)

a=[9,8,87,98]
b=999
print(firstIndex(a,0,b))