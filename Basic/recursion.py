#finding fibanachi number using recursio0n

def fiba(n):
    if(n==1 or n==2):
        return 1
    return fiba(n-1)+fiba(n-2)

a=int(input())
print(fiba(a))

