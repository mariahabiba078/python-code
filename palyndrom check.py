a=int(input("Enter a number:"))
b=a
d=0
while(a>0):
    c=a%10
    d=d*10+c
    a=a//10
if(b==d):
    print("This  is a palindrome!")
else:
    print("This is not a palindrome!")




















