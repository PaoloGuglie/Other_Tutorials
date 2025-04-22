from collections.abc import Callable  # better than using the typing module


def func(string: str) -> Callable[[], None]:  # function that takes no arguments
                                              # and returns None
    def wrapper() -> None:
        print("started")
        print(string)
        print("ended")

    return wrapper


def main() -> None:

    x = func('hello!')

    x()


if __name__ == '__main__':
    main()
