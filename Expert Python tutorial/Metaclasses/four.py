# A metaclass is "above" the classes I'm creating myself. When I create a class,
# the information I give is passed to a metaclass that takes it and returns an
# object that represents the class.

# To create a metaclass, I can inherit from "type".

# In a normal class, __new__(cls) returns an instance of the class:
#    return object.__new__(cls)
# In a metaclass, I return a class.

# Metaclasses can be used to enforce constraints. For example, I can have every class
# in a module to never be allowed to use a certain attribute or have an attribute.


class Meta(type):

    def __new__(self, class_name, bases, attrs):
        """ Called before __init__(). I can modify how an object is
        constructed by changing what happens here.
        The three arguments after "self" are the ones of
        type(name, bases, attrs).
        Creates the class. """

        print('\n', attrs)

        # "attrs" is a dictionary

        a = {key if key.startswith("__") else key.upper(): value
             for key, value in attrs.items()}

        print('\n', a)

        # return the class object itself:
        return type(class_name, bases, a)


# The default metaclass is "type". I've overwritten that to my
# own metaclass.
class Dog(metaclass=Meta):

    x = 5
    y = 8

    def hello(self):
        print("hi!")

# I used the metaclass to modify the construction of the Dog class. In this
# example, I used a dictionary comprehension to make all the methods and attributes
# of any child class, including Dog, into .upper() and return, using type(), these.


print("\n-------------------------\n")


def main() -> None:

    d = Dog()

    # If I now try to access the "x" I defined:

    try:
        print(d.x)

    except AttributeError:
        print("x is not an attribute of Dog!")

    # If I try to use the "X" I created with the dictionary comprehension:
    print('\nThe value of "X" is', d.X)


if __name__ == '__main__':
    main()
