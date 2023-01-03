class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res

inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.calculateFactorial())
    
