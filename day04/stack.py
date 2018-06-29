class Stack():
    def __init__(self):
        self.list = []

    def push(self,entry):
        self.list.append(entry)

    def pop(self):
        return self.list.pop(-1)

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return len(self.list) == 0

    def __str__(self):
        return str(self.list)

if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(5)
    print(stack.pop())
    print(stack.peek())
