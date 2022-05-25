'''
A function withou name(Anonymous Function)
Not Powerful as Named Function
It can work with Single Expression/ Single line of code 
'''
#This is Named Function
from ast import Expression

'''
def calculate(a,b):
    return a*a + 2*a*b +b*b
print(calculate(2,3))
'''


#lambda parameter:Expression 
try:
    a=(lambda a,b : a*a + 2*a*b +b*b) (2,3)
    b=(lambda c : c*c*c) (2)
    print("result: ",a)
    print("result: ",b)

except Exception as e:
    print(e)