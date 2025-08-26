
def invert_bst(self, root):
    if not root:
        return root
    
    temp = self.invert_bst(root.right)
    root.right = self.invert_bst(root.left)
    root.left = temp

    return root
