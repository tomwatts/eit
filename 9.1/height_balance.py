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


def get_tree_height_balance(root):
    left_height = 0
    right_height = 0
    left_balanced = True
    right_balanced = True

    if root.left is None and root.right is None:
        return (0, True)
    
    if root.left is not None:
        left_height, left_balanced = get_tree_height_balance(root.left)
        if not left_balanced:
            return (-1, False)

    if root.right is not None:
        right_height, right_balanced = get_tree_height_balance(root.right)
        if not right_balanced:
            return (-1, False)

    return (1 + max(left_height, right_height), (abs(left_height - right_height) <= 1) and left_balanced and right_balanced)


root = Node(314)

root.left = Node(6)
root.right = Node(6)

root.left.left = Node(271)
root.left.right = Node(561)
root.right.left = Node(2)
root.right.right = Node(271)

# A perfect tree
assert get_tree_height_balance(root)[1]

root.left.left.left = Node(28)
root.left.left.right = Node(0)

# Height difference of one still height balanced
assert get_tree_height_balance(root)[1]

root.left.right.right = Node(3)

# Still balanced...
assert get_tree_height_balance(root)[1]

root.left.right.right.left = Node(17)
root.left.right.right.left.left = Node(71)

# Balanced at root, but not balanced at one child
assert not get_tree_height_balance(root)[1]

