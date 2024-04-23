# Write a program to find the reverse of a number.
# Write a program to check if a number is a perfect number or not.


# online
# number = int(input("Enter the integer number: "))  
  
# # Initiate value to null  
# revs_number = 0  
  
# # reverse the integer number using the while loop  
  
# while (number > 0):  
#     # Logic  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
  
# # Display the result  
# print("The reverse number is : {}".format(revs_number)) 


# num = input("Enter the number: ")
# str1 = ''
# for i in num[::-1]:
#     str1 += i
# int1 = int(str1)
# print(int1)


# Write a program to check if a number is a perfect number or not.
# 6: Its proper divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.

number = int(input("Enter the number for checking: "))
num1 = 0
for i in range(1,number):
    if number%i == 0:
        num1 += i
if num1 == number:
    print("Is a perfect number")
else:
    print("Not a perfect number.")




