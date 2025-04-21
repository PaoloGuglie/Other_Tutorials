
for i in range(1, 11):
    def show():
        print(i * 2, end=" - " if i < 10 else "")

    show()

print("\nLast show: ", end=""); show()


print("\n\n-------------------------------\n")


def func(x):

    if x == 1:

        def rv():
            print("X is equal to 1")

    else:

        def rv():
            print("X is not 1")

    return rv


new_func = func(1)

new_func()
