class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        prev = None

        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right

        return True
        