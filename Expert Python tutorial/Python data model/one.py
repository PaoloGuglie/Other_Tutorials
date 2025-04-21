# Dunder methods are called Data Model methods because they are part of
# the Data Model.


class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'This person is called {self.name}.'

    def __mul__(self, x):
        """ Defines what happens when I use a multiplication operation on
        objects from this class """

        if type(x) is not int:
            raise Exception("Invalid argument, must be int.")

        return self.name * x

    def __call__(self, y):
        print(self.name, 'said "', y, '"')


def main() -> None:

    p = Person('Tim')
    print(p)

    print("\n-----------------------\n")

    print(p * 5)

    print("\n-----------------------\n")

    p('Hello!')


if __name__ == '__main__':
    main()
