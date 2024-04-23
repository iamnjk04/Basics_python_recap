# Write a program to count the number of even and odd numbers in a list.
length =int(input("How long do you want the list to be? "))
list1 = []
count_even, count_odd = 0,0
for i in range(length):
    content = int(input(f"Enter the {i} index content: "))
    list1.append(content)
    if list1[i]%2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"The list is {list1}")
print(f"The count of even numeber in the list {list1} is {count_even}")
print(f"The count of odd numeber in the list {list1} is {count_odd}")