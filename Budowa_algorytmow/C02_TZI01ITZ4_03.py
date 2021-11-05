import os
import platform
import random

"""--------------------------------------"""      
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")      
"""--------------------------------------"""      

"""--------------------------------------"""
"""--------------------------------------"""
def Main():
    
    
    y = input("x? = ")
    
    x = int(y)
    
    
    print(x+x)
    print(y+y)
  
"""--------------------------------------"""
MyClear()
Main()





