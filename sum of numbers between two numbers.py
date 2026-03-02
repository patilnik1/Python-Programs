sumofnumbers = 0

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for i in range(num1 + 1, num2):
    sumofnumbers += i

print("Sum of numbers between {} and {} : {}".format(num1, num2, sumofnumbers))