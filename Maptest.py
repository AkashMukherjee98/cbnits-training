#map and filter using for iterable object
'''
Iterable is an object which can be looped over or 
iterated over with the help of a for loop. 
Objects like lists, tuples, sets, dictionaries, strings, etc. 
are called iterables. In short and simpler terms, 
iterable is anything that you can loop over.
'''
from re import S


def square(x):
    return x*x

num =[1,2,3,4,5]
res=list(map(square,num))
print(res)

def show(s):
    return s+s
str=["A","K","A","S","H"]
result=list(map(show,str))
print(result)
