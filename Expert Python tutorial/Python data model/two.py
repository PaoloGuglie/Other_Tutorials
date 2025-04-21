from queue import Queue as q


# I want to create my Queue class, similar to the one in Python, with some addons:

class Queue(q):

    def __repr__(self):
        return f'Queue size: {self._qsize()}'

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()


def main() -> None:

    qu = Queue()

    print(qu)

    print("\n-----------------------\n")

    qu + 9; qu + 7; qu + 1
    qu - 2

    print(qu)


if __name__ == '__main__':
    main()
