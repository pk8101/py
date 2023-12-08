#sum of array using recursio0n

def sum1(l,s):
    if(len(l)==s):
        return 0
    return l[s]+sum1(l,s+1)

a=[9,8,9]
print(sum1(a,0))