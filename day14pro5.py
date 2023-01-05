class A:
    def first_method(self):
        print("Method of class A...")
class B:
    def first_method(self):
        print("Method of class B...")
##class C(A,B):
class C(B,A):    
    def third_method(self):
        print("Method of class C...")
if __name__=='__main__':
    ob=C()
    ob.first_method()
##    ob.second_method()
    ob.third_method()
