import os
from banner import banner
from ac import ac
def init(a):
    while a != "x":
         banner()
         a=input(' -- > ') 
         os.system('clear')
         if a == "1":
            print("here binary function 1")
            #f(a)
         elif a == "2":
            print("here octa funct 2:" )
            #f(a)
         elif a == "3":
            print("here octa funct 3:" )
            #f(a)
         elif a == "4":
            print("Here hex function 4:")
            ac()
         else:
            print("propably bad typo")
    return a
if __name__ =='__main__':
    a=''
    init(a)


