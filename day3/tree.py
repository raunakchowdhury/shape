class Tree():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_left(self,left):
        self.left = left

    def set_right(self,right):
        self.right = right

    def in_order_traversal(self):
        traversal = ''
        if self.left == None and self.right == None:
            return self.data
        traversal += self.left.in_order_traversal()
        traversal += self.data
        traversal += self.right.in_order_traversal()
        return traversal

    def pre_order_traversal(self):
        traversal = ''
        if self.left == None and self.right == None:
            return self.data
        traversal += self.data
        traversal += self.left.pre_order_traversal()
        traversal += self.right.pre_order_traversal()
        return traversal

    def post_order_traversal(self):
        traversal = ''
        if self.left == None and self.right == None:
            return self.data
        traversal += self.left.post_order_traversal()
        traversal += self.right.post_order_traversal()
        traversal += self.data
        return traversal

    def evaluate(self):
        total = 0
        if self.left == None and self.right == None:
            return int(self.data)
        total = self.left.evaluate()
        if self.data == '+':
            total += self.right.evaluate()
        if self.data == '*':
            total *= self.right.evaluate()
        if self.data == '-':
            total -= self.right.evaluate()
        if self.data == '/':
            total /= self.right.evaluate()
        return total

if __name__ == '__main__':
    tree = Tree('A',Tree('B',Tree('D'),Tree('E')),Tree('C'))
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())

    print('Attempting to calculate 5*(4+3):')
    calculator = Tree('*',Tree('5'),Tree('+',Tree('4'),Tree('3')))
    print(calculator.evaluate())

    print('Attempting to calculate 5/(4-3):')
    calculator = Tree('/',Tree('5'),Tree('-',Tree('4'),Tree('3')))
    print(calculator.evaluate())
    #calculator = Tree()
