'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--a", type=int, help="first")
parser.add_argument("--b", type=int, help="second")
'''
def getInput():
    f_no=int(input("Enter a no: "))
    s_no=int(input("Enter a no: "))
    return f_no,s_no
def add(): 
    x, y =getInput()
    return x + y
def sub(): 
    x,y=getInput()
    return x - y
def mul(): 
    x,y=getInput()
    return x * y
print ("1: add,2: sub,3: mul")
   
choice =int(input("Enter your choice: "))
operation =[add, sub, mul]

output =operation[choice-1]()
print("output",output)