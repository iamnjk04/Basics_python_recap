# Write a program to check if a given year is a leap year or not.
# Write a program to print the multiplication table of a given number.
# Write a program to convert Celsius to Fahrenheit and vice versa.

# year = int(input("Enter the year that you want to check: "))

# if year%400 == 0:
#     print(f"{year} is a leap year.")
# elif year%100 == 0:
#     print(year,"is not a leap year.")
# elif year%4 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# # Write a program to print the multiplication table of a given number.
# mul_number = int(input("Enter the number for it's multiplication table: "))
# upto_num = int(input("Upto which number do you want the table to be?  "))
# print("Table is: \n")
# for i in range(1,upto_num+1):
#     print(f"{mul_number}*{i}={mul_number*i}")



# Write a program to convert Celsius to Fahrenheit and vice versa.
choice = int(input("Enter \n1.To convert celsius to Fahrenheit. \n2.To convert Fahrenheit.\n"))

if choice == 1:
    temp = float(input("Give the temperature: "))
    print(f"{temp} degree celsius is equal to {temp * 33.8} degree Fahrenheit.")
elif choice == 2:
    temp = float(input("Give the temperature: "))
    print(f"{temp} degree Fahrenheit is equal to {temp / 33.8} degree Celsius.")