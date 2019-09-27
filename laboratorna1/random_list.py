import random

x = int(input("Enter the number of array elements: "))
y = int(input("Enter number for the beginning: "))
z = int(input("Enter number for the ending: "))

random_list = []
for i in range(x):
    random_list.append(random.randint(y, z))

print(random_list)
print("Sum - " + str(sum(random_list)))
print("Average - " + str(sum(random_list)/len(random_list)))
