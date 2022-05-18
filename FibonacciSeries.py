n=int(input("Enter a no: "))
first=0
second=1
fibo=0
for i in range(1,n+1,1):
    fibo=first+second
    print(fibo,end=" ")
    first=second
    second=fibo
