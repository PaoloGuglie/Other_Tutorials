# Decorator with function with arguments:

def function(func):

    def wrapper(*args, **kwargs):
        """ Using the unpack operator, the wrappers works both on functions
         that have arguments and functions that don't have arguments. """

        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper


@function
def ciao():
    print("Ciao!")


@function
def greet(x):
    print(f"Hello, {x}!")


def main() -> None:

    ciao()

    print("\n----------------------\n")

    greet('Paolo')


if __name__ == '__main__':
    main()
