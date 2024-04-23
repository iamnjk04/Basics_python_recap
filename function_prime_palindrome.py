from prime_palindrom_armstrong import prime_num, palindrome_num, armstrong_num
def choices():
    choice = int(input("Enter: \n1.To check prime number. \n2.To check the given number is a palindrome or not. \n3.To check if the numebr is armstrong or not.\n"))
    if choice == 1 : 
        prime_num()
    elif choice == 2 : 
        palindrome_num()
    elif choice == 3 : 
        armstrong_num()
    a = int(input("Enter \n0.To exit \n1.To main menu \n"))
    if a == 1:
        choices()
    else:
        exit
choices()

    