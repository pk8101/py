#custome error handling using class

class ZeroDenError(Exception):
    pass
a=int(input())
b=int(input())
try:
    
    if b==0:
        raise ZeroDenError('den must not be zero')
    c=a//b
except ZeroDenError:
    print("zero error")

else:  # here if no exception occur then else will be executed if except is executed then else will not be executed
    print(c)