class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def top(self):
        self.stack[-1]


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)
        if self.left is not None:
            self.left.PrintTree()
        if self.right is not None:
            self.right.PrintTree()


def binary_tree_depth_order(root):
    result = Stack()
    nodes = [root]
    while nodes:
        result.push([n.data for n in nodes])
        child_nodes = list()
        for n in nodes:
            if n.left is not None:
                child_nodes.append(n.left)
            if n.right is not None:
                child_nodes.append(n.right)
        nodes = child_nodes

    return result.stack


root = Node(314)

root.left = Node(6)
root.right = Node(6)

root.left.left = Node(271)
root.left.right = Node(561)
root.right.left = Node(2)
root.right.right = Node(271)

root.left.left.left = Node(28)
root.left.left.right = Node(0)
root.left.right.right = Node(3)
root.right.left.right = Node(1)
root.right.right.right = Node(28)

root.left.right.right.left = Node(17)
root.right.left.right.left = Node(401)
root.right.left.right.right = Node(257)

root.right.left.right.left.right = Node(641)

assert binary_tree_depth_order(root) == [[314], [6, 6], [271, 561, 2, 271], [28, 0, 3, 1, 28], [17, 401, 257], [641]]
