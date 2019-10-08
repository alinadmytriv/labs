import random


# create a random list
def create_list(x0, y0, z0):
    random_list = []
    for i in range(x0):
        random_list.append(random.randint(y0, z0))
    return random_list


# summarize the elements of the list
def summary(list0):
    return sum(list0)


# find the average of the list
def average(list1):
    return summary(list1)/len(list1)


# the main function which ask to input details about the list
def main():
    x = int(input("Enter the number of array elements: "))
    y = int(input("Enter number for the beginning: "))
    z = int(input("Enter number for the ending: "))
    l = create_list(x, y, z)
    print("Random list - " + str(l))
    print("Sum - " + str(summary(l)))
    print("Average - " + str(average(l)))


# call the main function
if __name__ == "__main__":
    main()

