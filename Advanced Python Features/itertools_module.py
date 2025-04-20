# The itertools in Python is a library that allows me to get access to more
# advanced iterators in Python.

import itertools


def main() -> None:

    # Infinite iterators
    counter = itertools.count(start=10, step=2)
    print(next(counter))
    print(next(counter))

    print("\n-------------------------\n")

    # Cicle through a finite sequence infinitely
    cycler = itertools.cycle(['A', 'B', 'C'])
    print(next(cycler), end=' - ')
    print(next(cycler), end=' - ')
    print(next(cycler), end=' - ')
    print(next(cycler))

    print("\n-------------------------\n")

    # Create combinations (or permutations) of elements
    combinations = itertools.combinations('ABC', 3)
    print(list(combinations))


if __name__ == '__main__':
    main()
