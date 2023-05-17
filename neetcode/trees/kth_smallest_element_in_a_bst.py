# Given the root of a binary search tree, and an integer k, return the kth
# smallest value (1-indexed) of all the values of the nodes in the tree.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        self.addNodeToStack(root, stack)

        # At every iteration, the top of the stack represents the smallest.
        while k > 1:
            self.addNodeToStack(stack.pop().right, stack)
            k -= 1

        return stack[-1].val

    # Adds the smallest node in the given node (tree) to the top of the stack,
    # as well as all the nodes it touches on the way down.
    def addNodeToStack(self, node, stack): 
        while node:
            stack.append(node)
            node = node.left
