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
    y = x
  
    if y<0:
        y = -y
    print(f"|{x}| = {y}")
  
"""--------------------------------------"""
MyClear()
Main()

