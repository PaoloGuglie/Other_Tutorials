# Create a context manager using a generator:

from contextlib import contextmanager


# contextlib offers a decorator I can use on a generator to make it into a context
# manager:

@contextmanager
def file_manager(filename, method='r'):
    print(' - enter')
    file = open(filename, method)
    yield file
    file.close()
    print(' - exit')


def main() -> None:

    with file_manager('write.txt', 'w') as file:
        print(' - middle')
        file.write('The cat is in the box!')


if __name__ == '__main__':
    main()
