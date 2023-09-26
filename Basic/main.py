a=int(input())
l=[]
for i in range(a):
    l.append(int(input()))

a=set()
for s in l:
    a.add(s)

print(len(l)-len(a))