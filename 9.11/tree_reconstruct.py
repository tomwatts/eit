class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def PreOrder(self):
        s = self.data
        if self.left is not None:
            s += self.left.PreOrder()
        if self.right is not None:
            s += self.right.PreOrder()
        return s

    def PrintTree(self):
        print(self.PreOrder())


def reconstruct_tree(inorder, preorder):
    if not (inorder and preorder):
        return None

    root = Node(preorder[0])
    if len(preorder) == 1:  # Leaf!
        return root

    left_inorder = inorder[0:inorder.find(preorder[0])]
    left_preorder = preorder[1:len(left_inorder) + 1]

    root.left = reconstruct_tree(left_inorder, left_preorder)

    right_inorder = inorder[len(left_inorder) + 1:]
    right_preorder = preorder[len(left_inorder) + 1:]

    root.right = reconstruct_tree(right_inorder, right_preorder)

    return root


assert reconstruct_tree('FBAEHCDIG', 'HBFEACDGI').PreOrder() == 'HBFEACDGI'
assert reconstruct_tree('DCEBFHGAJLMKNIOP', 'ABCDEFGHIJKLMNOP').PreOrder() == 'ABCDEFGHIJKLMNOP'
