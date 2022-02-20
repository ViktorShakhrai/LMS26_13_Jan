# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.
import collections


class Stack:
    def __init__(self):
        self.__stack = collections.deque()

    def add(self, dataval):
        self.__stack.append(dataval)

    def remove(self):
        if len(self.__stack) <= 0:
            # return ("No element in the Stack")
            raise StopIteration
        else:
            return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def __iter__(self):
        return self

    def __next__(self):
        return self.remove()


if __name__ == '__main__':
    data = "Hello world"
    stack = Stack()
    for i in data:
        stack.add(i)
    print(len(stack))
    for i in stack:
        print(i)
