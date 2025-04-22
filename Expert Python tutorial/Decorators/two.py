# Decorators's simplicity:

def function(func):

    def wrapper():
        print("Started")
        func()
        print("Ended")

    return wrapper


def greet():
    print("Hello!")


def ciao():
    print("Ciao!")


@function                # decorator
def salutations():
    print("Salutations!")


def main() -> None:

    # Reassigning:
    x = function(greet)
    x()

    print("\n----------------------\n")

    # I can use a shortcut:
    global ciao
    ciao = function(ciao)
    ciao()

    print("\n----------------------\n")

    # Using the decorator:
    salutations()


if __name__ == '__main__':
    main()
