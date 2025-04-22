import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        total = round(time.time() - start, 2)
        print(f"\nFunction execution took {total} seconds.")

    return wrapper


@timer
def test():
    for _ in range(100_000_000): pass


def main() -> None:
    test()


if __name__ == '__main__':
    main()
