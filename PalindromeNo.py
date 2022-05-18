def palindromeNo(no):
    rev=0
    temp=no
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no=no//10
    if(rev==temp):
        print("The No",temp,"is Palindrome No")
    else:
        print("The No",temp,"is Not Paindrome")

def sumOfDigit(no):
    sum=0
    while(no>0):
        rem=no%10
        sum=sum+rem
        no=no//10
    print("The Sum Of Digit Is: ",sum)

def armstrongNo(no):
    temp=a=no
    count=0
    sum=0
    while(temp!=0):
        count=count+1
        temp=temp//10
    while(a!=0):
        pow=1
        rem=a%10
        for i in range(1,count+1,1):
            pow=pow*rem
        sum=sum+pow
        a=a//10
    if(sum==no):
        print("The No is: ",no," Armstrong No")
    else:
        print("The No is: ",no," Not Armstrong No")
                        
no=int(input("Enter a no: "))
palindromeNo(no)
sumOfDigit(no)
armstrongNo(no)

