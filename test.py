class Car:
    def __init__(self):
        self.en=None
        self.fr=None
        self.fl=None
        self.br=None
        self.bl=None
class Engine:
    def __init__(self,cc):
        self.cc=cc
class Wheel:
    def __init__(self,size):
        self.size=size

a=Car()
a.en=Engine(1000)
a.fr=Wheel(50)
a.fl=Wheel(50)
a.br=Wheel(50)
a.bl=Wheel(50)


class Car1():
    def __init__(self):
        self.en=None
        self.wls=None

b=Car1()
b.en=Engine(2500)
b.wls=[]
for i in range(4):
    tmp=Wheel(50)
    b.wls.append(tmp)
print(b.wls[2].size)







