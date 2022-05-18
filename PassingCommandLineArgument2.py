import sys

print("ss",sys.argv)


print("aa: ",sys.argv[1])

no=sys.argv[1]

'''
n=("Enter the no: "+int(no))
'''
n=(int(no))
print("num: ",n)

first=0
second=1
fibo=0
for i in range(1,n+1,1):
    fibo=first+second
    print(fibo,end=" ")
    first=second
    second=fibo
