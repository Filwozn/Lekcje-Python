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
        tmp = x
        x = y
        y = tmp
    
    print(f"{x}, {y}")
  
"""--------------------------------------"""
MyClear()
Main()

