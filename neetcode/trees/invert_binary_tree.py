 # Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, obj):
        if not obj: 
            return False
        if not isinstance(obj, TreeNode): 
            return False
        return (self.val == obj.val 
                and self.left == obj.left
                and self.right == obj.right)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))

    def invertTreeV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        root.left, root.right = root.right, root.left
        self.invertTreeV2(root.left)
        self.invertTreeV2(root.right)
        return root

    def invertTreeV3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left: 
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return root

s = Solution()

t1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
t2 = TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None))

assert s.invertTree(t1) == t2

t3 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
t4 = TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None))

assert s.invertTreeV2(t3) == t4

t5 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
t6 = TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None))

assert s.invertTreeV3(t5) == t6

print('ALL TESTS PASS')
        
