class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        curr = root
        res = []
        stack = []

        while curr or stack:
            if curr:
                res.append(curr)
                stack.append(curr.right)
                curr = curr.left
            else:
                cur = stack.pop()
        return res