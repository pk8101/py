#finding fact for large number using recursio0n
import sys
sys.setrecursionlimit(9000)
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


a=int (input())
print(fact(a))