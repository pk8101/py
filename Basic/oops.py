#inheriting object class
# object class contains three methods :
# 1.def __new__():-> this method used to create new object
# 2.def __init__():-> this method used to initiate new object
# 3.def __str__():-> this method used to give the description for the class
class circle (object):
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return "this is an circle class which takes radius as an argument"

s=circle(20)
print(s)





