#fraction class

class Fraction:
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den

f=Fraction(2,3)
print(f.__dict__)

