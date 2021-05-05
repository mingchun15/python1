from math import pi
class Circle():
    def __init__(self,radius=1.0):
        self.radius=radius
    def setradius(self,radius):
        self.radius=radius
    def getradius(self):
        return  self.radius
        return pi*self.radius*self.radius 

b=Circle(4)
print(b.get_area())

class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

a=Point()
print(a.x)
print(a.y)

class Rectangle:
    def __init__(self,length=0.0,width=0.0):
        self.length=length
        self.width=width
    def get_area(self):
        return self.length*self.width
    def get_meter(self):
        return (self.length+self.width)*2
    
d = Rectangle(3,4)
print(d.get_area())
print(d.get_meter())


class Square:
    def __init__(self,length=0.0):
        self.length=length
    def setlength(self,length):
        if(length<0):
            print("error happend")
        else:
            self.length=length
    def getlength(self):
        return self.length*4
    


#tw/edu/nkust/ic/c109156215/shape.py 是 uml package
