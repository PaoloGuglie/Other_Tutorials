# Python has a better way to create generators using the Generator Pattern:

def gen(n):
    for i in range(n):
        yield i ** 2

# The "yield" keyword returns the value and pauses the function. I can keep track of
# the state of execution.


def main() -> None:

    g = gen(11)
    for i in g: print(i, end=" ")

    print("\n\n-------------------\n")

    b = gen(3)

    print(next(b), end=" - "); print(next(b))


if __name__ == '__main__':
    main()
