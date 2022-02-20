class Node:
    def __init__(self, data):
        self.data = data
        self.hand = None
        self.index = None


class Stack:
    def __init__(self):
        self.root: Node = None

    def push(self, data):
        '''Add data to  top of stack'''
        n = Node(data)
        n.index = self.__add_index_to_node__()
        if not self.root:
            self.root = n
        else:
            n.hand = self.root  # Вузол що прийшов в руку приймає попередній рут
            self.root = n  # Новий вузол стає рутом

    def pop(self):
        '''Pop data from top of stack'''
        if self.root is None:
            raise IndexError("No data!")
        ret = self.root
        self.root = ret.hand
        return ret.data

    def __add_index_to_node__(self) -> int:
        '''Add index for node in stack'''
        if self.root is None:
            return 0
        return self.root.index + 1

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.index


if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    s.push('d')
    s.pop()
print(len(s))
