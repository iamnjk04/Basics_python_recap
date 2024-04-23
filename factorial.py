# Write a program to find the factorial of a number.
fact_number = int(input("Enter the number to be factorized:"))
num = 1
for i in range(1,fact_number+1):
    num = num*i
print(f"The factorial of {fact_number} is {num}")