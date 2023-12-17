#multiple inheriting 
class A:
    def hi(self):
        print("its class A")

class B:
    def hello(self):
        print("its class B")
class C(A,B):
    def __init__(self):
        print("its class C")
s=C()
s.hello()
s.hi()






