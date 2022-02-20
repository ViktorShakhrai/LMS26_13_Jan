class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == 0

    def add_to_queue(self, data):
        self.queue.append(data)

    def remove_from_queue(self):
        if self.is_empty():
            print("Queue is empty!")
            exit(1)
        data = self.queue.pop(0)
        return data

    def del_queue(self):
        print("Deliting queue")
        del self.queue
