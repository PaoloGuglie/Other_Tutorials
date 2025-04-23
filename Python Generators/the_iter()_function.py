def main() -> None:

    x = range(1, 11)

    # If I try this:
    try:
        print('\n', next(x))

    except TypeError as e:
        print(f'\nError: {e}.')

    # To make x into an iterator, I have to use iter() or .__iter__() :
    x = iter(x)
    print(f'\nCorrect version: {next(x)}, {next(x)}, {next(x)}...\n')

    # When I write:
    for i in range(4): print(i, end=" ")

    print("\n")

    # I am referring to:
    for i in iter(range(4)): print(i, end=" ")


if __name__ == '__main__':
    main()
