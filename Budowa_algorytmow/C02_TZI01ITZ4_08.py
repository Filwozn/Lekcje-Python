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
        
    x = int(input("x? = "))    
    y = int(input("y? = "))    
    
    
    
    if x>y:
        max = x
    else:
        max = y
    print(f"Max({x}, {y}) = {max}")
  
"""--------------------------------------"""
MyClear()
Main()

