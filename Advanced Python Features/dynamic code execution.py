def demonstrate_exec() -> None:
    """ I use the local scope to test this code because I am inside a
    function when exec() executes the code, so everything is stored in
     the local scope. """

    code = """def greet(name):
        return f"Hello, {name}!"
        """

    local_scope = {}

    exec(code, {}, local_scope)

    print('\n', local_scope["greet"]("Alice"))


def demonstrate_eval() -> None:
    """ I can type demonstrate_exec() into this input, and it will
    be executed: this shows the risk of running / modifying code from
    eval().
    I can type demonstrate_eval() to create a recursive call. """

    expression = input("Type an expression: - ")

    result = eval(expression)

    print(f"\nResult of eval: {result}")


def demonstrate_safe_eval() -> None:
    """ The variables are passed in the local scope. In evaluating the
    expression, eval() only has access to what's been defined in the local
    scope. I cannot access other functions or variables. """

    expression = input("Type an expression that uses a, b and c: ")

    variables = {'a': 2, 'b': 3, 'c': 4}

    result = eval(expression, {}, variables)

    print(f"Result of safe eval: {result}")


def main() -> None:

    demonstrate_exec()

    print("\n-----------------\n")

    demonstrate_eval()

    print("\n-----------------\n")

    demonstrate_safe_eval()


if __name__ == '__main__':
    main()
