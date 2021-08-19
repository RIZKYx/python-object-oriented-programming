class A:

    def show(self):
        print('ini adalah show a')

class B(A):

    pass

class C(A):

    pass

class D(B,C):
    pass

objek = D()
objek.show()
#help(objek)