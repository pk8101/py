class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
a.next=b
print(a)
print(a.data)
print(a.next)
print(b)
print(b.data)
print(b.next)