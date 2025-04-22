# I can make a class by doing this:

Test = type('Test', (), {})  # args: class_name, inheritances, attributes

# It's equivalent to:
#   class Test:
#       pass


def main() -> None:

    print(Test)


if __name__ == '__main__':
    main()
