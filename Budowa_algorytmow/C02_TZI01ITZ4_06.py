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
    
    if x>5:
        print(f"{x}>5")
  
"""--------------------------------------"""
MyClear()
Main()

"""
x? = 6
|6| = 6
"""

"""
x? = -4
|-4| = 4
"""
#8, 6, 6, 4, 4, 4, 3 ...


