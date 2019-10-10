# decorator for escaping html tags
def decor_html(func):
    def read_file(str0):
        # create a file that will include text with escaped html tags
        new_file = open("new-html-file.txt", "w")
        # create a file that will include text with escaped html tags
        tags = {"<": "&lt;", ">": "&gt;", "&": "&amp;", "\"": "&quot;"}
        for x in func(str0):
            if x in tags.keys():
                x = tags[x]
                new_file.write(x)
            else:
                new_file.write(x)
        new_file.close()
        # read the created file
        with open("new-html-file.txt") as nf:
            print(nf.read())
    return read_file


# function for decorator
@decor_html
def open_file_for_escape(string):
    with open(string) as f:
        text = f.read()
    return text

# function which just open and read the file
def open_file(string):
    with open(string) as f:
        text = f.read()
    return print(text)

# the main function
def main():
    a = input("Do you want to escape html tags(escape) or read the file(read) or exit(exit)? - ")
    if a == "escape":
        file3 = input("Write the file name: ")
        open_file_for_escape(file3)
    elif a == "read":
        file3 = input("Write the file name: ")
        open_file(file3)
    else:
        print("Bye-Bye")

# call the main function
if __name__ == '__main__':
    main()