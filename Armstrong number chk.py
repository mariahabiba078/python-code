#A positive integer is called an Armstrong number of order n if abcd... = an+bn+cn+dn+... in case of an Armstrong number of 3 digits,the sum of the cubes of each digit is equal to the number itself



num = int(input("Enter the number to check:"))
sum = 0
temp = num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num == sum:
        print( num,"is an Armstrong number")
else:
        print( num,"is not an Armstrong number")
