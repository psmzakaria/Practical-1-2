# Question 1 

# Write codes for the incomplete program below so that it sums up all the digits in the integer variable num (9+3+2) and displays the output as a sum.

num = int(input("Enter your Number Here"))
print(num)

# Getting the first digit number
digit1 = int(num/100)
print(digit1)

# Getting the second digit number
digit2 = (int(num/10) % 10)
print(digit2)

# Getting the third digit number
digit3 = (num % 10)
print(digit3)

sum = digit1 + digit2 + digit3
print(sum)