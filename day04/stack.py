class Stack():
    def __init__(self):
        self.list = []

    def push(self,entry):
        self.list.append(entry)

    def pop(self):
        return self.list.pop(-1)

    def peek(self):
        return self.list[-1]

if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(5)
    print(stack.pop())
    print(stack.peek())
