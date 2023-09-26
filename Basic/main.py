# print('hello world')
# a={1:2,2:4,5:9}
# print(a.keys())
# print(a.values())
# d=a.copy()
# print(d)
# print(d.items())
# #dict are mutable
# f={2:5}
# a.update(f)
# a.pop(5)
# print(a)
# del a[1]
# print(a)

a=int(input())
l=[]
for i in range(a):
    e=int(input())
    l.append(e)
d={}
for j in l:
    d[j]=d.get(j,0)+1

print(max(d.values()))