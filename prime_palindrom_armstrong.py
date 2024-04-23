# # Write a program to check if a number is prime or not.
# Write a program to check if a given string is a palindrome.
# Write a program to check if a number is Armstrong or not.

def prime_num():
    num = int(input("Enter the number: "))
# Program to check if a number is prime or not


# define a flag variable
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

    # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")


# Write a program to check if a given string is a palindrome.
def palindrome_num():
    str1 = input("Give the string:")
    str2 = ""
# j = len(str1)
# print(type(j))
    for i in str1[::-1]:
        str2 += i
    if str1 == str2:
        print(f"Given string {str1} is a palindrome")
    else:
        print(f"Given string {str1} is not a palindrome")

# Write a program to check if a number is Armstrong or not.
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
def armstrong_num():
    arm_number = input("Give a number to check if its armstrong: ")
    armed_number = int(arm_number)
    arm_number = list(arm_number)
    armstrong = 0
    for i in range(len(arm_number)):
        armstrong += (int(arm_number[i]))**3
    if armed_number == armstrong:
        print(f"{armed_number} is an Armstrong number.")
    else:
        print(f"{armed_number} is not an Armstrong number.")



# Python program to check if the number is an Armstrong number or not #from the internet

# take input from the user
# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    print(digit)
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
