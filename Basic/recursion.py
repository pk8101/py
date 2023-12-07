#power of numbers using recursio0n

def powern(a,b):
    if(b==1):
        return a
    return a*powern(a,b-1)

a=int(input())
b=int(input())
print(powern(a,b))