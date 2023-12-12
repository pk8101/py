#replace pi with 3.14 in array using recursio0n

def replace(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        return '3.14'+replace(s[2:])
    else:
        return s[0]+replace(s[1:])
         
    


a="fnvlifnpiojnvsnpi"
b=999
print(replace(a))