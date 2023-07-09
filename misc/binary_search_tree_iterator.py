# Implement the BSTIterator class that represents an iterator over the in-order
# traversal of a binary search tree (BST):

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.addNodeToStack(root)

    def addNodeToStack(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        next_node = self.stack.pop()
        self.addNodeToStack(next_node.right)
        return next_node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Our stack represents the call stack when doing DFS (left preference). 
# Adding a node to the stack means:
#   - Going left until no longer possible (like in recursive DFS).
#   - As we traverse left, adding the nodes we touch to the stack.
#       - This allows us to return to unfinished calls (explore the right side).
# At any point after we finish adding. We know that the top of the stack has our
# next smallest node.
# We can prove this using the idea of an invariant: 
#   - Our stack starts off when the smallest node at the top, since we
#     simply go left from the root. 
#   - In the next method, we pop the smallest off, then call addNodeToStack
#     with the smallest.right.
