# Given the root of a binary tree, determine if it is a valid BST.

# A valid BST is defined as follows:

# - The left subtree of a node contains only nodes 
#   with keys less than the node's key.
# - The right subtree of a node contains only nodes
#   with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root, left_bound, right_bound): 
        if not root:
            return True
        if not (left_bound < root.val < right_bound):
            return False
        return self.isValidBSTHelper(root.left, left_bound, root.val) and \
                self.isValidBSTHelper(root.right, root.val, right_bound)

    def isValidBSTV2(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, float('-inf'), float('inf')]]
        while stack: 
            curr, left_bound, right_bound = stack.pop()
            if curr:
                if not (left_bound < curr.val < right_bound): 
                    return False
                stack.append([curr.left, left_bound, curr.val])
                stack.append([curr.right, curr.val, right_bound])
        return True

