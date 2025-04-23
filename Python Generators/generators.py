def main() -> None:

    y = map(lambda x: x ** 2, [1, 2, 3, 4])

    # This loop:
    for i in y: print(i, end=" ")

    print("\n------------------")

    y = map(lambda x: x ** 2, [1, 2, 3, 4])

    # Is the same as:
    while True:

        try:
            value = next(y)
            print(value, end=" ")

        except StopIteration:
            print("\nDone!")
            break

    print("\n------------------")

    y = map(lambda x: x ** 2, [1, 2, 3, 4])

    # And the same as:
    while True:

        try:
            value = y.__next__()
            print(value, end=" ")

        except StopIteration:
            print("\nDone!")
            break


if __name__ == '__main__':
    main()
