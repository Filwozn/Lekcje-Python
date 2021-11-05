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
    z = int(input("z? = "))    
    
    x1 = x
    y1 = y
    z1 = z
    
    if x1>y1:
        tmp = x1
        x1 = y1
        y1 = tmp
    

    if y1>z1:
        tmp = z1
        z1 = y1
        y1 = tmp


    if x1>y1:
        tmp = x1
        x1 = y1
        y1 = tmp

    
    print(f"({x}, {y}, {z}) -> ({x1}, {y1}, {z1})")
  
"""--------------------------------------"""
MyClear()
Main()

"""
x =? 9
y =? 5
z =? 1

(9, 5, 1) -> (1, 5, 9)

"""
#12, 9, 9, 6, 6, 6, 3...
