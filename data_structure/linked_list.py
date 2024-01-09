class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None
        self.__length: int = 1
        self.list_data: list = []

    def __add_element(self, data):
        new = Node(data)
        self.list_data.append(data)
        if self.__head:
            new.previous = self.__tail
            self.__tail.next = new
            self.__tail = self.__tail.next
        else:
            self.__head = new
            self.__tail = self.__head
        self.__length += 1

    def add(self, data):
        if isinstance(data, list | tuple | set):
            for d in data:
                self.__add_element(d)
        else:
            self.__add_element(data)

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
        while key:
            current = current.next
            key -= 1
        current.data = value

    def __str__(self):
        current = self.__head
        body = []
        while current:
            tmp = current.data
            if isinstance(tmp, LinkedList):
                tmp = tmp.list_data
            body.append(tmp)
            current = current.next
        return f'LinkedList: {body}'

    def __add__(self, additive):
        result = LinkedList()
        result.add(self.list_data + additive.list_data)
        return result

    def __len__(self):
        return self.__length
