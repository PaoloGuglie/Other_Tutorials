# A context manager handles the processing of a file. It handles automatically
# closing the file for me when an error occurs or the operations are performed
# successfully.

with open('info.txt', 'r') as f:
    contents = f.read()
    print(contents)

print("\n-----------------------\n")


# I can mimic the behavior of a context manager

class FileManager:
    """" When I create my own context manager, I have to override an __enter__()
    and __exit__() method. These functions allow me to use the "with" syntax."""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """ Automatically called when "with FileManager(...)" is used. It
        performs some initial setup operations. """

        # Open the file
        self.file = open(self.filename, self.mode)
        print(f"Opening file {self.filename}")

        return self.file  # this allows me to use the "as" syntax.

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ When I exit the context manager, it performs some teardown
        operations. It takes an exception type, value and traceback.
        This function is still called if an error occurs inside the
        context manager, allowing for proper file closure anyway. """

        # Close the file
        self.file.close()
        print(f"Closing file {self.filename}")

        # Handle exceptions
        if exc_type:
            print(f"An exception occurred: {exc_val}")

        return True  # to suppress exceptions, if needed


def main() -> None:

    with FileManager('info.txt', 'r') as file:
        contents = file.read()
        print(contents)


if __name__ == '__main__':
    main()
