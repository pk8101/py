#simple inheritance 

class A:
    def __init__(self,name):
        print("hello ",name)
    def hello(self):
        print("hello its class a")
class B (A):
    def __init__(self, name):
        super().__init__(name)
        print("its class b")
        
s=B('pradeep')





