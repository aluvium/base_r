### Init
import os
from banner import banner
from ac import ac
from bina import bina
def init(a):
    while a != "x":
         banner()
         a=input(' -- > ') 
         os.system('clear')
         if a == "1":
            print("Here binary --> ASCII --> character function 1:")
            bina()
         elif a == "2":
            print("here octa funct 2:" )
            #f(a)
         elif a == "3":
            print("here hex funct 3:" )
            #f(a)
         elif a == "4":
            print("Here ASCI --> characters function 4:")
            ac()
         else:
            print("Propably bad typo, please try again. Pick up the number from 1 - 4 or x for exit. ")
    return a
if __name__ =='__main__':
    a=''
    init(a)


