class Foo:
    def show(self):
        print('hi')


def add_attribute(self):
    self.z = 9


Test = type('Test', (Foo,), {'x': 5, "add_attribute": add_attribute})


def main() -> None:

    t = Test()
    print(t.x)

    print("\n----------------------------\n")

    # I can define attributes outside the class:
    t.w = 'Hello!'
    print(t.w)

    print("\n----------------------------\n")

    t.show()

    print("\n----------------------------\n")

    t.add_attribute()

    print(t.z)


if __name__ == '__main__':
    main()
