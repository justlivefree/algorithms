from abc import ABC


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class BaseLinkedList(ABC):

    def __init__(self):
        self._head = None
        self._tail = None
        self._current = None
        self._length: int = 0
        self.list_data: list = []

    def _add_element(self, data, d=1):
        """
        :param d: 1 -> right, 0 -> left
        """
        new = Node(data)
        if self._head:
            if d:
                new.previous = self._tail
                self._tail.next = new
                self._tail = self._tail.next
            else:
                new.next = self._head
                self._head.previous = new
                self._head = self._head.previous
        else:
            self._head = new
            self._tail = self._head
        self.list_data.append(data)
        self._length += 1

    def _pop_left(self):
        if tmp := self._head:
            data = tmp.data
            self._head = tmp.next
            if tmp.next:
                self._head.previous = None
            else:
                self._tail = None
            del tmp
            return data
        raise IndexError(f'{self.__class__.__name__} is empty')

    def _pop_right(self):
        if tmp := self._tail:
            data = tmp.data
            try:
                self._tail = tmp.previous
                self._tail.next = None
            except AttributeError:
                self._head = None
            del tmp
            return data
        raise IndexError(f'{self.__class__.__name__} is empty')

    def __str__(self):
        current = self._head
        body = []
        while current:
            tmp = current.data
            if isinstance(tmp, LinkedList):
                tmp = tmp.list_data
            body.append(tmp)
            current = current.next
        return f'{self.__class__.__name__}: {body}'


class LinkedList(BaseLinkedList):

    def add(self, data):
        if isinstance(data, list | tuple | set):
            for d in data:
                self._add_element(d)
        else:
            self._add_element(data)

    def remove(self, index):
        if index >= self._length or index < 0:
            raise IndexError('Index out of range')
        current = self._head
        while index and current.next:
            current = current.next
            index -= 1
        if current.previous:
            current.previous.next = current.next
        else:
            self._head = current.next
        if current.next:
            current.next.previous = current.previous
        else:
            self._tail = current.previous
        self._length -= 1

        del current

    def pop(self):
        return self._pop_right()

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        data = self._current.data
        self._current = self._current.next
        return data

    def __getitem__(self, index):
        if index > self._length:
            raise IndexError('Index is out of range')
        if index < 0:
            index = -1 * index - 1
        current = self._head
        while index:
            current = current.next
            index -= 1
        return current.data

    def __setitem__(self, key, value):
        if key > self._length:
            raise IndexError('Index is out of range')
        current = self._head
        while key:
            current = current.next
            key -= 1
        current.data = value

    def __add__(self, additive):
        result = LinkedList()
        result.add(self.list_data + additive.list_data)
        return result

    def __bool__(self):
        return bool(self._length)

    def __len__(self):
        return self._length

