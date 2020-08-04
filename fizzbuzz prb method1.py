#So the problem is basically to give you the numbers 1 to 100, if the number is divisible by 3, print
# 'Fizz', if divisible by 5, print 'Buzz', if divisible by 3 and 5, print 'FizzBuzz'. For other numbers
# just print out the number itself."
for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
