import inspect
from queue import Queue


def func(x):

    if x == 1:

        def rv():
            print("X is equal to 1")

    else:

        def rv():
            print("X is not 1")

    return rv


def main() -> None:

    new_func = func(2)

    print(inspect.getmembers(new_func))

    print("\n------------------\n")

    print(inspect.getsource(new_func))

    print("\n------------------\n")

    print(inspect.getsource(Queue))


if __name__ == '__main__':
    main()
