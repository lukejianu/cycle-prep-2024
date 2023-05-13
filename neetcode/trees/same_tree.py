# Given the roots of two binary trees p and q, write a function to check if they
# are the same or not.

# Two binary trees are considered the same if they are structurally
# identical, and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True

        if not p or not q: 
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeV2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack:
            t1, t2 = stack.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            stack.append([t1.left, t2.left])
            stack.append([t1.right, t2.right])
        return True

