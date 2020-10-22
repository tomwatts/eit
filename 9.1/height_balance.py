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


def get_tree_height(root):
    left_height = 0
    right_height = 0

    if root.left is None and root.right is None:
        return 0
    
    if root.left is not None:
        left_height = get_tree_height(root.left)

    if root.right is not None:
        right_height = get_tree_height(root.right)

    return 1 + max(left_height, right_height)


def is_height_balanced(root):
    return abs(get_tree_height(root.left) - get_tree_height(root.right)) <= 1


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

assert is_height_balanced(root)

root.right.left.right.left.right.right = Node(641)
assert not is_height_balanced(root)
