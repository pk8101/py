from datetime import date
class pradeep:
    def __init__(self,year):
        #self.age=age
        self.year=year
        #print("hi pradeep ur age",self.age)
    @classmethod
    def calculateage(cls,year):
        return cls(date.today().year-year)
    @staticmethod
    def hello():
        print("hello pradeep")

s1=pradeep(23)
s1.hello()
