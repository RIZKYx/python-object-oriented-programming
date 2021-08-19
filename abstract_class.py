  # membuat class abstract

from abc import ABC, abstractclassmethod

class button(ABC):

    def click(self):
        pass

class pushbutton(button):

    def click(self):
        print('push button click')

class radiobutton(button):

    def click(self):
        print('radio button click')

tombo1 = pushbutton()
tombol2 = radiobutton()


tombo1.click()
tombol2.click()