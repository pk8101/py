# sum of n natural  numbers using recursio0n


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


a = int(input())
print(sum(5))
