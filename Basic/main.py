#custome error handling in this we use raise keyword
a=int(input())
b=int(input())
try:
    c=a//b
    raise ZeroDivisionError

except ZeroDivisionError:
    print("zero error")