#multiple inheriting finding method resolution order
class A:
    def hi(self):
        print("its class A")

class B:
    def hi(self):
        print("its class B")
class C(A,B):
    def __init__(self):
        print("its class C")
s=C()
s.hi()
print(C.mro())






