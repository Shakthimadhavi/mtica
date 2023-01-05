class A:
    def first_method(self):
        print("Method of class A...")
class B:
    def second_method(self):
        print("Method of class B...")
class C(A,B):
    def third_method(self):
        print("Method of class C...")
if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.second_method()
    ob.third_method()
