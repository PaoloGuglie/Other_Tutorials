# If I have a very large file to read, I can use generators to store one line of
# the file at a time to look for data

def file_reader(filename):
    for row in open(filename, 'r'):
        yield row


# There is a way to create a generator without creating a function; I can use a
# generator comprehension:

x = (i for i in range(10))

# I can use it with:
squares = (x * x for x in range(10) if x % 2 == 0)
# I get lower memory usage, but it's possibly slower than a list comprehension.


def main() -> None:

    file = file_reader('info.txt')

    for row in file:
        print('-', row)

    print("\n----------------------------\n")

    y = [i for i in range(10)]
    print('List from a list comprehension:', y)

    print('Generator from a tuple comprehension:', x)


if __name__ == '__main__':
    main()
