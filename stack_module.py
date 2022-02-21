class Node:
    def __init__(self, data):
        self.data = data
        self.left_hand = None
        self.right_hand = None
        self.index = None


class Stack:
    def __init__(self):
        self.root: Node = None
        self.end: Node = None

    def push(self, data):
        '''Add data to  top of stack'''
        n = Node(data)
        n.index = self.__add_index_to_node__()
        if not self.root:
            self.root, self.end = n, n
        else:
            n.right_hand = self.root  # Той хто прийшов повинен взяти нас в праву руку
            self.root.left_hand = n  # Попередня голова повинна взяти в ліву руку новий вузол
            self.root = n  # Назначаємо нову голову

    def pop(self, index: int = None):
        '''Pop data from top of stack'''
        if index:
            if index < 0 or index > (len(self) - 1):
                raise ValueError('Index out of range')
            data = None
            for i in self:
                if data:
                    if i.data == index:
                        local_previous = i.right_hand
                        local_next = i.left_hand
                        local_previous.right_hand = local_next
                        local_next.left_hand = local_previous
                        data = i.data
                else:
                    i.index += 1
            if data:
                return data
            else:
                raise ValueError(f'No data! with index:{index}')
        else:
            if self.root is None:
                raise IndexError("No data!")
            ret = self.root
            self.root = ret.right_hand
            return ret.data

    def __add_index_to_node__(self) -> int:
        '''Add index for node in stack'''
        if self.root is None:
            return 0
        return self.root.index + 1

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.index + 1

    def __getitem__(self, item: int):
        '''Primitive get_item ,returned only  root'''
        return self.root.data

    def __iter__(self):
        self.__local_node = self.end
        return self

    def __next__(self):
        if self.__local_node is None:
            raise StopIteration
        n = self.__local_node
        self.__local_node = self.__local_node.left_hand
        return n


if __name__ == '__main__':
    s = Stack()
    s.push('f')
    s.push('4')
    s.push('6')
    s.push('g')
    s.push('t')
    s.pop()
    for i in s:
        print(i.data)
