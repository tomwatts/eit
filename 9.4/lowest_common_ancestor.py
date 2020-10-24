class Node:

    def __init__(self, data, parent=None):

        self.left = None
        self.right = None
        self.parent = parent
        self.data = data


    def PrintTree(self):
        print(self.data)
        if self.left is not None:
            self.left.PrintTree()
        if self.right is not None:
            self.right.PrintTree()


def lowest_common_ancestor(n_0, n_1):
    if (n_0.parent is None) or (n_1.parent is None):
        return None

    p_0 = n_0.parent
    while (p_0):
        p_1 = n_1.parent
        while (p_1):
            if (p_0 == p_1):
                return p_0
            p_1 = p_1.parent
        p_0 = p_0.parent

    return None


root = Node(314)
root.left = Node(6, root)
root.right = Node(6, root)

root.left.right = Node(561, root.left)
root.right.left = Node(561, root.right)

root.left.right.right = Node(3, root.left.right)

root.right.left.left = Node(3, root.right.left)

assert lowest_common_ancestor(root, root.left) is None
assert lowest_common_ancestor(root.left, root.right) == root
assert lowest_common_ancestor(root.left.right, root.left.right.right) == root.left
assert lowest_common_ancestor(root.right.left.left, root.left.right) == root

another_root = Node(1)
another_root.left = Node(2, another_root)
another_root.left.left = Node(3, another_root.left)
assert lowest_common_ancestor(root.right.left.left, another_root.left.left) is None
