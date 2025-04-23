# How to create an iterator using the old synthax (not the generator synthax):


class Iter:

    def __init__(self, *args):

        if len(args) == 1:
            self.current = 0
            self.end = args[0]

        elif len(args) == 2:
            self.current, self.end = args

        else:
            raise TypeError(f"Expected 1 or 2 arguments, but {len(args)} were provided!")

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.end:
            raise StopIteration

        current = self.current

        self.current += 1

        return current


def main() -> None:

    print("Using range():", end=" ")
    for i in range(4): print(i, end=" ")
    print("\nUsing Iter():", end=" ")
    for i in Iter(4): print(i, end=" ")

    print("\n-------------")

    print("Using range():", end=" ")
    for i in range(2, 6): print(i, end=" ")
    print("\nUsing Iter():", end=" ")
    for i in Iter(2, 6): print(i, end=" ")

    print("\n-------------")

    x = Iter(5)

    print(next(x), end=" "); print(next(x))


if __name__ == '__main__':
    main()
