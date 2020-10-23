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


def is_symmetric(root):
    if root is None:
        return True

    level_nodes = [root.left, root.right]
    while level_nodes:
        left = 0
        right = len(level_nodes) - 1
        while left < right:
            ln = level_nodes[left]
            rn = level_nodes[right]
            if ln and rn and (ln.data != rn.data) or (ln is None) ^ (rn is None):
                return False
            left += 1
            right -= 1

        next_level_nodes = list()
        for n in level_nodes:
            if n:
                next_level_nodes += [n.left, n.right]
        level_nodes = next_level_nodes

    return True


assert is_symmetric(None)

root = Node(314)
root.left = Node(6)
root.right = Node(6)
root.left.right = Node(561)
root.right.left = Node(561)
assert is_symmetric(root)

# Structurally asymmetric
root.left.right.right = Node(3)
assert not is_symmetric(root)

root.right.left.left = Node(3)
assert is_symmetric(root)

# Structurally symmetric, but differing keys
root.right.left.left.data = Node(4)
assert not is_symmetric(root)
