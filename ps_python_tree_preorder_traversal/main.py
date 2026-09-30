def preorder_traversal(self, root):
    res = []
    if root:
        res.append(root.data)
        res = res + self.preorder_traversal(root.left)
        res = res + self.preorder_traversal(root.right)
    return res
