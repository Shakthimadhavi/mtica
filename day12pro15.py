class Rectangle:
    def __init__(self,width,length):
        assert(length>=0 and width>=0),'INVALID'
        self.width=width
        self.length=length
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp

       

l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    peri=ob.calculatePerimeter()
    print('Area of rectangle is',area)
    print('Perimeter of rectangle is',peri)

except AssertionError as obj:
    print(obj)
