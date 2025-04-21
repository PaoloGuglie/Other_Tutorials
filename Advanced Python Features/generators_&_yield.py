# Generators are a more modern version of the iterator and work by using a "yield"
# keyword inside a Python function. Using it allows me to pause execution of a
# function and only execute a little bit of code, return a value and pause and
# wait until I am asked for the next value to generate.

# They are use when I want space efficient execution or calculations.

# It can give me each value one by one and only store one value at a time when I
# need to use it. No need to actually generate all values.

# To yield = cedere, produrre, dare, fornire, rendere...

def count_up_to(max_value: int):
    """ A generator function that yields numbers from 1 up to max_value.
    Generators automatically implement the next() funtion to grab the
    next value. """

    current = 1

    while current <= max_value:
        yield current  # yield the current value and pause execution. Wait at this
                       # line until the next value is requested.
        current += 1


def main() -> None:

    # Create a generator object:
    counter = count_up_to(10)
    print(counter)

    print("--------")

    # Get the first values by manually calling next():
    print(next(counter))
    print(next(counter))
    print(next(counter))

    print("--------")

    # Iterate to get the remaining values (it calls next() automatically):
    for i in counter: print(i)


if __name__ == '__main__':
    main()
