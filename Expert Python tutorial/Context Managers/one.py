# Context managers are used when dealing with shared memory and resources, locking /
# unlocking...


def main() -> None:

    file = open('../notes.txt', 'r')
    print('\n', file.read())
    file.close()

    # If there is an error in the .read() line, the program's execution may stop and
    # the file would never close.

    print("\n-------------------------\n")

    # I can use a try-except:

    file = open('../notes.txt', 'r')

    try:
        print(file.read())

    finally:
        file.close()

    print("\n-------------------------\n")

    # Or I can use a context manager ("with" keyword):

    with open('../notes.txt', 'r') as file:
        print(file.read())

    # The __exit__() method is always called, even if exceptions arise. This method
    # closes the file properly.


if __name__ == '__main__':
    main()
