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

def convert_infix_to_postfix(string):
    stack = Stack()
    converted_string = ''
    for char in string:
        #print(stack)
        if char == '*' or char == '/' or char == '(':
            stack.push(char)
        elif char == '+' or char == '-':
            #pop off everything in the stack, unless it's in a nested parentheses
            while not stack.isEmpty():
                if stack.peek() == '(':
                    break
                converted_string += stack.pop()
            stack.push(char)
        elif char == ')':
            # Pop down to the first '(' that appears
            while not stack.isEmpty():
                popped_entry = stack.pop()
                if popped_entry != '(':
                    converted_string += popped_entry
                else:
                    break
        else:
            converted_string += char
    #If there are other operators in the stack, pop them and add them to the stack
    while not stack.isEmpty():
        converted_string += stack.pop()
    return converted_string

if __name__ == '__main__':
    strings = ['32+5*','32/5*','32-5*']
    for string in strings:
        expression_tree = build_expression_tree(string)
        print('Evaluating', string, ':', expression_tree.evaluate())

    strings = ['3+2*5','(3+2)*5','(3*(4+5)+5)','(3*(4*5)+5)']
    for string in strings:
        converted_string = convert_infix_to_postfix(string)
        print('Evaluating', string, ':', converted_string)
        expression_tree = build_expression_tree(converted_string)
        print('Evaluating', converted_string, ':', expression_tree.evaluate())
