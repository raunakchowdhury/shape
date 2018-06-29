from tree import Tree
from stack import Stack

def build_expression_tree(string):
    stack = Stack()
    for char in string:
        if char == '+' or char == '-' or char == '*' or char == '/':
            stack.push(Tree(char,stack.pop(),stack.pop()))
        else:
            stack.push(Tree(char))
    return stack.pop()

'''
# another implementation: use a try-catch loop
try:
    if type(int(char)) is int:
    stack.push(Tree(char))
except ValueError:
    stack.push(Tree(char,stack.pop(),stack.pop()))
    print(stack.peek())
return stack.pop()
'''

if __name__ == '__main__':
    expression_tree = build_expression_tree('32+5*')
    print(expression_tree.evaluate())
    expression_tree = build_expression_tree('32/5*')
    print(expression_tree.evaluate())
    expression_tree = build_expression_tree('32-5*')
    print(expression_tree.evaluate())
