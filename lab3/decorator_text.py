# decorator text with html tags
def html_tag(tag=""):
    def html_decorator(func):
        def wrap(text1):
            print("<" + tag + "> " + func(text1) + " </" + tag + ">")
        return wrap
    return html_decorator

# function for decorator
@html_tag("p")
def html_string(text0):
    return text0

# a main function which ask to input text
# which will be inside the html tags
def main():
    s = input("Enter text fot html tags: ")
    return html_string(s)

# call the main function
if __name__ == '__main__':
    main()