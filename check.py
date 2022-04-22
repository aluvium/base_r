### File exist check
import os
def fcheck():
    chck = False
    while chck is False:
        print("Provide valid path to a file:")
        x=input(" -- > ")
        chck=os.path.isfile(x)
        print("[[ ** The path is incorrect. ** ]]")
    return x
