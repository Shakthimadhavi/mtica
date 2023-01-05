##class Cat:
##    def __init__(self,color,legs):#instance attributes
##        self.color=color
##        self.legs=legs
##    def __str__(self):
##        temp="cat is "+self.color +' color '+' and has ' +str(self.legs)+' legs '
##        return temp
##
##if __name__=="__main__":
##    pet1=Cat("ginger",4)
##    print(pet1.legs)
##    print(pet1.color)
##    print(pet1)
##
##    pet2=Cat("brown",3)
##    print(pet2.color)
##    print(pet2.legs)
##    print(pet2)


##class Dog:
##    price=400
##    def __init__(self,name,color):
##        self.color=color
##        self.name=name
##    def bark(self):
##        print("Woof")
##        print(self.name, "has " ,self.price,
##              "price and its color is ", self.color)
##        
##if __name__=='__main__':
##    pet1=Dog("Tommy","brown")
##    pet2=Dog("sheru","white")
##    pet1.bark()
##    pet2.bark()
##    print(pet1.price)
##    print(pet2.price)
##    print(Dog.price)
##    Dog('abc','blue').bark()

##class Wolf:
##    price=500
##    def __init__(self,name,color):
##        self.name=name
##        self.color=color
##    def bark(self):
##        print("Grr...")
##class Dog(Wolf):
##    def bark1(self):
##        print("Woof")
##
##if __name__=="__main__":
##    pet1=Dog("tomy","brown")
##    pet1.bark()
##    pet1.bark1()
##    print(pet1.name," is of colour ",pet1.color)
##


##class Animal:
##    def __init__(self,name,color):
##        self.name=name
##        self.color=color
##class Cat(Animal):
##    def mew(self):
##        print("Cat meows")
##class Dog(Animal):
##    def bark(self):
##        print("Woof")
##if __name__=="__main__":
##    print(__name__)
##    pet1=Dog("tomy","brown")
##    pet2=Cat("lucky","white")
##    pet1.bark()
##    pet2.mew()
##    print(pet1.name)
##    print(pet2.name)


class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr...")
class Dog(Wolf):
    def bark(self):
        print("Woof")
pet1=Dog("tomy","brown")
pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()
