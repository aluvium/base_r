### Function ASCI -- > char
import os
from check import fcheck

def ac():
    x=fcheck()
    with open( x ,'r') as f:
        e=f.read()
        os.system('clear')
        print("[[ ** Printing recived file ** ]]")
        print(f'{e}\n')
        d=e.split()
        dd=''
        for each in d:
            dd+=chr(int(each))
        print("[[ ** Printing decoded file ** ]]")
        print(f'{dd}\n\n')    
        f.close()
    return None
