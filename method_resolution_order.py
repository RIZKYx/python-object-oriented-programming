class A:

    def show(self):
        print('ini adalah show a')

class B:

    def show(self):
        print('ini adalah show b')

class c(B,A):
    pass

objek = c()
objek.show()
# help(objek)