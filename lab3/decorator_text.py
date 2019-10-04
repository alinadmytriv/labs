def html_decorator(func):
    def wrap(*args):
        s = func(*args)
        print("<" + s[0] + "> " + s[1] + " </" + s[0] + ">")
    return wrap


@html_decorator
def html_string(*args):
    return args


t = input("Enter html tag: ")
s = input("Enter text fot html tags: ")
html_string(t, s)

