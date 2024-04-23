# Write a Python function to find the maximum of three numbers.
# Create a function to calculate the factorial of a given number.

choice = int(input("Enter: \n1.To find max of three numbers. \n2.To calculate the factorial of number. \n"))

def max_num(first_num, second_num, third_num):
    if first_num >= second_num and first_num >= third_num:
       print(first_num,"is the max")
    elif second_num >= first_num and second_num >= third_num:
       print(second_num,"is the max")
    elif third_num >= second_num and third_num >= first_num:
       print(third_num,"is the max")

def fact_num():
   fact_number = int(input("Enter the number toi calculate the factorial: "))
   num = 1
   for i in range(1,fact_number+1):
      num *= i
   print(f"Factorial of {fact_number} is {num}")


if choice == 1:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    third_num = int(input("Enter the third number: "))
    max_num(first_num,second_num,third_num)

elif choice == 2:
   fact_num()

