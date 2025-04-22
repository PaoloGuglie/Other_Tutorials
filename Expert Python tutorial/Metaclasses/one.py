# In Python, classes are objects.
# A metaclass defines the rules for a class. When I create a class, I call a "type"
# constructor.
# Everything in Python is an object.


class Test:
    pass


def main() -> None:

    print(Test)

    print("This is the metaclass:", type(Test))


if __name__ == '__main__':
    main()
