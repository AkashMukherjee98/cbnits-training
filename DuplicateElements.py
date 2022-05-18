from msilib.schema import DuplicateFile
from multiprocessing.dummy import Array
from xml.dom.minidom import Element


a=[]
n=int(input("Enter the range of array:"))
print("Enter the elements")
for i in range(0,n):
   l=int(input())
   a.append(l)
print("Show the elements in an array: ")
print(a,end=" ")
print()
len=len(a)
print("Show the Duplicate Elements from the Array")
c=0
for i in range(0,len):
    for j in range(i+1,len):
        if(a[i]==a[j]):
            c=c+1
            print(a[j],end=" ")
print()
print("Total Duplicate Elements Are: ",c)