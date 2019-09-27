# decorator for escaping html tags
def decor_html(func):
    def read_file(str0):
        s = func(str0)
        # create a file that will include text with escaped html tags
        new_file = open("new-html-file.txt", "w")
        for x in s:
            if x == "<":
                x = "&lt;"
                new_file.write(x)
            elif x == ">":
                x = "&gt;"
                new_file.write(x)
            elif x == "&":
                x = "&amp;"
                new_file.write(x)
            elif x == "\"":
                x = "&quot;"
                new_file.write(x)
            else:
                new_file.write(x)
        new_file.close()
        # read the created file
        new_file = open('new-html-file.txt', "r")
        print(new_file.read())
        new_file.close()
    return read_file


# function for decorator
@decor_html
def open_file_for_escape(string):
    file = open(string, "r")
    text = file.read()
    file.close()
    return text


# function which just open and read the file
def open_file(string):
    file = open(string, "r")
    text = file.read()
    file.close()
    return print(text)


a = input("Do you want to escape html tags(escape) or read the file(read) or exit(exit)? - ")
if a == "escape":
    file3 = input("Write the file name: ")
    open_file_for_escape(file3)
elif a == "read":
    file3 = input("Write the file name: ")
    open_file(file3)
else:
    print("Bye-Bye")
