a=[]
n=int(input("Enter the range of array:"))
print("Enter the elements")
for i in range(0,n):
   l=int(input())
   a.append(l)
print("Show the elements in an array: ")
print(a,end=" ")
print()
print("Enter the search element")
k=int(input())
print(k)
for i in range(0,n):
    if(a[i]==k):
        flag=1
        print("value found at: ",(i+1))
        break
if(flag==0):
    print("value not found")