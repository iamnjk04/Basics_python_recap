# Write a program to find the maximum number in a list.
length = int(input("How long do you want the list to be? "))
list1 = []
max_num, min_num = 0, 0 
for i in range(length):
    content = int(input(f"Enter the {i} index content: "))
    list1.append(content)
    if content > max_num:
        max_num = content
    elif content <= min_num:
        min_num = content
print(f"The list is {list1}")
print(f"The max number in the list {list1} is {max_num}")
print(f"The min number in the list {list1} is {min_num}")