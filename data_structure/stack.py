from data_structure.linked_list import BaseLinkedList


class Stack(BaseLinkedList):
    def pop(self):
        return self._pop_right()

    def push(self, data):
        self._add_element(data)
