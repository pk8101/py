a=int(input())
l=[]
l1=[]
for i in range(a):
    l.append(int(input()))

d={}
for j in l:
    d[j]=d.get(j,0)+1
for f in d:
    if d[f]>=2:
        l1.append(f)
h=[]
for b in l1:
    for x in range(len(l)):
        if b==l[x]:
            h.append(x)
t=len(h)-1
h1=0
while(t>=0):
    h2=h[t]-h[t-1]
    if h2>h1:
        h1=h2
    t=t-2
print(h1)
