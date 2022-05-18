import argparse

try:
    def getInput():
        parser = argparse.ArgumentParser()
        parser.add_argument("--a", type=int, help="first")
        parser.add_argument("--b", type=int, help="second")
        args = parser.parse_args()
        f_no=args.a
        s_no=args.b
        return f_no,s_no
except:
    print("first write --a and take integer value then write --b take integer value ")
    
def add(): 
    x, y =getInput()
    return x + y
def sub(): 
    x,y=getInput()
    return x - y
def mul(): 
    x,y=getInput()
    return x * y
def div(): 
    x,y=getInput()
    return x // y
def exit(): 
    return "run again"

print ("1: add,2: sub,3: mul 4:div 5.Exit")
choice =int(input("Enter your choice: "))
#operation =[add, sub, mul, div, exit]
#output =operation[choice-1]()
#print("output",output)

while(choice!=5):
    if(choice>=1):
        operation =[add, sub, mul, div, exit]
        output =operation[choice-1]()
        print("output",output)
        print ("1: add,2: sub,3: mul 4:div 5.Exit")
        choice =int(input("Enter your choice: ")) 
    elif(choice==5):
        exit()
    
'''   
choice =int(input("Enter your choice: "))
operation =[add, sub, mul, div, exit]
output =operation[choice-1]() 
print("output",output)
'''
    

