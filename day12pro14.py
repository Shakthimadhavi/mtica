class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        temp=self.pi*self.radius**2
        return temp
    def calculatePerimeter(self):
        temp=2*self.pi*self.radius
        return temp
        

r=int(input())


ob=Circle(r)
area=ob.calculateArea()
peri=ob.calculatePerimeter()
print('Area of circle with radius ',r,'is',area)
print('Perimeter of circle with radius ',r,'is',peri)

