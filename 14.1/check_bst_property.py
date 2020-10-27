class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def InOrder(self):
        r = list()
        if self.left is not None:
            r += self.left.InOrder()

        r.append(self.data)

        if self.right is not None:
            r += self.right.InOrder()

        return r


def check_bst_tree(root):
    inorder = root.InOrder()
    for i in range(1, len(inorder) -1):
        if inorder[i - 1] > inorder[i]:
            return False

    return True


# Tree from page 251
root = Node(19)

root.left = Node(7)
root.left.left = Node(3)
root.left.left.left = Node(2)
root.left.left.right = Node(5)
root.left.right = Node(11)
root.left.right.right = Node(17)
root.left.right.right.left = Node(13)

root.right = Node(43)
root.right.left = Node(23)
root.right.left.right = Node(37)
root.right.left.right.right = Node(41)
root.right.left.right.left = Node(29)
root.right.left.right.left.right = Node(31)
root.right.right = Node(47)
root.right.right.right = Node(53)

assert check_bst_tree(root)

root.right.left.right.left.right = Node(3100)
assert not check_bst_tree(root)
