# Decorators with returns:

def function(func):

    def wrapper(*args, **kwargs):
        print("Started")
        total = func(*args, **kwargs)
        print("Ended")

        return total

    return wrapper


@function
def my_sum(x: int, y: int) -> int:
    print("summing...")

    return x + y


def main() -> None:
    number = my_sum(2, 9)
    print("-----------")
    print(number)


if __name__ == '__main__':
    main()
