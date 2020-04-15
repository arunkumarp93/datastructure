from tree.tree import BinaryTree
from stack.stack import Stack
import operator

def result(exp):

    stack = Stack()
    etree = BinaryTree('')
    exp_list = list(exp)

    #remove empty characters
    characters = [ item for item in exp_list if item != ' ']
    currentTree = etree
    stack.push(etree)

    for character in characters:
        if character == '(':
            currentTree.insert_left('')
            stack.push(currentTree)
            currentTree = currentTree.get_left()

        elif character not in ['+', '-', '*', '/', ')']:
             try:
                 currentTree.set_data(int(character))
                 parent = stack.pop()
                 currentTree = parent
             except:
                  raise ValueError("token '{}' is not a valid integer".format(character))

        elif character in ['+', '-', '*', '/']:

            currentTree.set_data(character)
            currentTree.inset_right('')
            stack.push(currentTree)
            currentTree = currentTree.get_right()

        elif character == ')':
            currentTree = stack.pop()
    return etree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.get_left()
    rightC = parseTree.get_right()

    if leftC and rightC:
        fn = opers[parseTree.get_data()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.get_data()

exp = '(3+(4*5))'

exp_tree = result(exp)

# exp_tree.post_order()

# exp_tree.pre_order()

# exp_tree.in_order()


print(evaluate(exp_tree))
