class Queue():
    def __init__(self):
        self.list = []

    def enque(self,entry):
        self.list.append(entry)

    def deque(self):
        return self.list.pop(0)

    def length(self):
        return len(self.list)
