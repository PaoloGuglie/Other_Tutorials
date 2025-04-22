# I can use more than one yield:

def gen(n):
    for i in range(n):
        yield i
        yield i ** 2
        yield i ** 3
        print("----")


def main() -> None:

    g = gen(10)

    for i in g:
        print(f" - {i}")


if __name__ == '__main__':
    main()
