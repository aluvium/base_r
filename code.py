### Initialize
import os
from banner import banner
from ac import ac
from bina import bina
from hexa import hexa
from octa import octa
def init(a):
    while a != "x":
         banner()
         a=input(' -- > ') 
         os.system('clear')
         if a == "1":
             print("Change binary --> decimal --> ascii characters: ")
             bina()
         elif a == "2":
             print("Change octal --> decimal --> ascii characters: " )
             octa()
         elif a == "3":
             print("Change hexadecimal --> decimal --> ascii character: " )
             hexa()
         elif a == "4":
             print("Change decimal  --> ascii characters:")
             ac()
         else:
             if a!='x':
                 print("Propably bad input, please try again. Pick up the number from 1 - 4 or x for exit. ")
             else:
                 print("Goodbye.")
    return 0
if __name__ =='__main__':
    a=''
    init(a)
