import sys

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


print("Enter a no: ",sys.argv)
n=sys.argv[1]
no=int(n)
palindromeNo(no)
