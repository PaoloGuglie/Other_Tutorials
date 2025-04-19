def main() -> None:

    # The Asterisk operator allows me to collect multiple elements:
    a, b, *c = [1, 2, 3, 4, 5]

    print(f"a: {a}\n"
          f"b: {b}\n"
          f"c:{c}")

    print("\n--------------------------\n")

    a, *b, c = [1, 2, 3, 4, 5]

    print(f"a: {a}\n"
          f"b: {b}\n"
          f"c:{c}")

    print("\n--------------------------\n")

    # To ignore a value, use the Anonymous variable:
    # (the underscore is a convention, still assigned)
    d, _, e = [1, 2, 3]

    print(f"d: {d}\n"
          f"_: {_}\n"
          f"e: {e}\n")

    print("\n--------------------------\n")

    # I can unpack nested structures:
    data = ("Alice", (25, "Engineer"))
    name, (age, profession) = data

    print(f"name: {name}\n"
          f"age: {age}\n"
          f"profession: {profession}")

    print("\n--------------------------\n")

    # I can unpack in function arguments:
    def print_names(*names):
        for i in names:
            print(" - ", i)

    print_names("Bob", "Ted", "Charlie")

    print("\n--------------------------\n")

    # I can combine lists with the Asterisk operator:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [33, 44, 55]

    combined_list = [*list1, *list3, *list2]

    print(f"Combined lists: {combined_list}")

    print("List2:", *list2)

    print("\n--------------------------\n")

    # I can unpack dictionaries:
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    combined_dict = {**dict1, **dict2}

    print(f"Combined dictionary: {combined_dict}")

    print("\n--------------------------\n")

    # Swapping variables using unpacking:
    # (without using a temporary variable)
    x, y = 10, 20
    print(f"Before swap - x: {x}, y: {y}")
    x, y = y, x
    print(f"After swap - x: {x}, y: {y}")


if __name__ == '__main__':
    main()
