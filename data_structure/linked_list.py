class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    __head: Node = None
    __tail: Node = None
    __length: int = 1
    __current: Node = None

    def add(self, data):
        if self.__head:
            self.__tail.next = Node(data)
        else:
            self.__head = Node(data)
            self.__tail = self.__head

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        data = self.__current.data
        self.__current = self.__current.next
        return data

    def __getitem__(self, index):
        if index > self.__length or index < 0:
            raise IndexError('Index is out of range')
        current = self.__head
        while index:
            current = current.next
            index -= 1
        return current.data

    def __setitem__(self, key, value):
        if key > self.__length:
            raise IndexError('Index is out of range')
        current = self.__head
        if key == 0:
            new = Node(value)
            new.next = current
            self.__head = new
        else:
            while key - 1:
                current = current.next
                key -= 1
            new = Node(value)
            new.next = current.next
            current.next = new

    def __len__(self):
        return self.__length

    def __str__(self):
        current = self.__head
        body = []
        while current:
            body.append(current.data)
            current = current.next
        return 'LinkedList(%s) at %s' % (body, hex(id(self)))
