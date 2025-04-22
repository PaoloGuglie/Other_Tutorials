# In a computer, there is a finite amount of memory (RAM).

def a():
    """ This can cause a MemoryError """

    x = [i ** 2 for i in range(100_000_000_000)]
    for i in x: print(i)


def b():
    """ I can avoid creating the list """

    for i in range(100_000_000_000): print(i)


class Gen:
    """ I only keep track of the internal state of the next number to generate """

    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        """ Next item in the iterable, in a loop or when next() is called """

        if self.last == self.n:
            raise StopIteration()

        return_value = self.last ** 2
        self.last += 1

        return return_value


def main() -> None:

    g = Gen(11)

    while True:

        try:
            print(next(g))

        except StopIteration:
            break


if __name__ == '__main__':
    main()
