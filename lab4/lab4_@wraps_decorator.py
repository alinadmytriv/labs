# wraps decorator
def wraps(func):
    def wraps_decorator(func1):
        def wrapper(*args):
            return func1(*args)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return wraps_decorator

# decorator for
def decorator(mult1):
    @wraps(mult1)
    def wrap(*args):
        print("multiplication = " + str(mult1(*args)))
    return wrap

# function that multiplies the numbers
@decorator
def mult(x, y):
    """does the multiplication"""
    return x*y

# the main function
def main():
    print(mult.__name__)
    print(mult.__doc__)
    print(help(mult))

# calls the main function
if __name__ == '__main__':
    main()

