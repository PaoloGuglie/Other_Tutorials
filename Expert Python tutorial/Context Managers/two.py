# Create a context manager:

class File:

    def __init__(self, filename, method='r'):
        self.file = open(filename, method)

    def __enter__(self):
        """ First thing that happens: returns some value used in the context
        manager. """

        print(" - Enter")

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Regardless of exceptions, this method is called.
        This code runs before the exception crashes the program, allowing me
        to take action. """

        if exc_val:
            print("--------- EXCEPTION ---------")
            print(f"Exception type: {exc_type}\n"
                  f"Exception traceback: {exc_tb}")
            print("-----------------------------")

        print(" - Exit")

        self.file.close()

        # To handle the exception, to avoid crashing:
        return True


def main() -> None:

    # Code with no exception:
    with File('../notes.txt') as f:
        print(" - Middle")
        f.read()

    print("\n-------------------------\n")

    # Code with exception:
    with File('../notes.txt') as f:
        print(" - Middle")
        f.read()
        raise Exception()


if __name__ == '__main__':
    main()
