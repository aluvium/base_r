### Function octal -- > decimal -- > ASCI
import os
from check import fcheck
from output import output

def octa():
    x=fcheck()
    with open( x ,'r') as f:
        e=f.read()
        os.system('clear')
        output()
        print("[[ ** Printing recived file ** ]]")
        print(f'{e}\n')
        d=e.split()
        b=''
        bb=''
        dd=''
        for each in d:
             b=(int(each, base=8))       
             bb+=str(b)+"  "
             dd+=chr(b)
        print("[[ ** Printing decoded file ** ]]")
        print(f"Decimal -- > {bb}")
        print(f'ASCII   -- > {dd}\n\n')    
        f.close()
    return None
