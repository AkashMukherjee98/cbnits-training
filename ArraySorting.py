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
print("len ",len)
print("Desending Order: ")
for i in range(0,len):
    for j in range(i+1,len):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    print(a[i],end=" ")
print()
print("Assending Order: ")
for i in range(0,len):
    for j in range(i+1,len):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    print(a[i],end=" ")