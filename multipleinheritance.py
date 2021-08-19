 class A:
    def method_A(self):
        print('ini adalah method A')

class B :
    def method_B(self):
        print('ini adalah method B')

class c(A,B):
    pass

object = c()

object.method_A()
object.method_B()