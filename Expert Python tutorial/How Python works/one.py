# In Python, a lot of the code is executed at run time, not compile time. So,
# this code will run without errors, even though I did not create a .bark()
# method. As long as I don't create an object out of the Dog class, I will not
# try to call the method and I won't get any errors.

class Dog:
    def __init__(self):
        self.bark()


# I can define a class inside a function:

def make_class(x):

    class Dog:

        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

        def print_name(self):
            print(self.name)

    return Dog


cls = make_class(10)

d = cls('Tim')
d.print_value()
d.print_name()
