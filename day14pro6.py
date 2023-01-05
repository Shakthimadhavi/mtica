class A:
    def first_method(self):
        print("Method of class A...")
class B(A):
    def first_method(self):
        print("Method of class B...")
        super().first_method()
ob=B()
ob.first_method()
    
