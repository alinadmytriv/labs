import random

# create a random list
def create_list(number, begin, end):
    random_list = []
    for i in range(number):
        random_list.append(random.randint(begin, end))
    return random_list

# summarize the elements of the list
def summary(list0):
    return sum(list0)

# find the average of the list
def average(list1):
    return summary(list1) / len(list1)

# ask to input details about the list
def input_number():
    numb = int(input("Enter the number of array elements: "))
    beg = int(input("Enter number for the beginning: "))
    end = int(input("Enter number for the ending: "))
    return numb, beg, end

# output the results
def output(list2):
    print("Random list - " + str(list2))
    print("Sum - " + str(summary(list2)))
    print("Average - " + str(average(list2)))

# the main function
def main():
    x, y, z = input_number()
    list = create_list(x, y, z)
    output(list)

# call the main function
if __name__ == "__main__":
    main()