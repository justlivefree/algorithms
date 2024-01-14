from data_structure.linked_list import BaseLinkedList


class SimpleQueue(BaseLinkedList):

    def deque(self):
        return self._pop_left()

    def enqueue(self, data):
        self._add_element(data)


class DoubleQueue(BaseLinkedList):

    def push_right(self, data):
        return self._add_element(data)

    def push_left(self, data):
        return self._add_element(data, 0)

    def pop_left(self):
        return self._pop_left()

    def pop_right(self):
        return self._pop_right()
