def inorder_traversal(self, root):
    res = []
    if root:
        res = self.inorder_traversal(root.left)
        res.append(root.data)
        res = res + self.inorder_traversal(root.right)
    return res
