class MyRange:
    """ An iterator is a Python class containing two dunder methods: __next__()
    and __iter()__"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """ The __iter__() method makes this class an iterable. It is
        called with iter().
        It should return an iterator object. """

        return self

    def __next__(self):
        """ The __next__() method defines the iteration behavior. It should
        return the next item in the sequence or raise StopIteration. """

        if self.current < self.end:
            value = self.current
            self.current += 1

            return value

        else:
            raise StopIteration


def main() -> None:

    r = range(5)
    itr = iter(r)  # returns an iterator

    while True:
        try:
            value = next(itr)
            print(value)
        except StopIteration:
            break

    print("\n--------------------------\n")

    my_range = MyRange(1, 5)

    # Behind the scenes, I am calling the __iter__() method on my_range, that returns
    # an iterator. Then the __next__() method is used as I cycle through all the values
    # in the range.
    for i in my_range: print(i, end=" " if i < my_range.end - 1 else "")
    # ( I used the ternary operator)


if __name__ == '__main__':
    main()
