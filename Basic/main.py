print('hello world')
a={1:2,2:4,5:9}
print(a.keys())
print(a.values())
d=a.copy()
print(d)
print(d.items())
#dict are mutable
f={2:5}
a.update(f)
a.pop(5)
print(a)
del a[1]
print(a)
