# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthV2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        maxDepthSoFar = 1
        stack = [[root, 1]]
        while stack:
            curr, depth = stack.pop()
            maxDepthSoFar = max(maxDepthSoFar, depth)

            if curr.left:
                stack.append([curr.left, depth + 1])
            if curr.right:
                stack.append([curr.right, depth + 1])

        return maxDepthSoFar

