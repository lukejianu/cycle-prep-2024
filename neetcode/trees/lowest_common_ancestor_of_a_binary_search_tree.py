# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Swap so that p.val <= q.val.
        if q.val < p.val: 
            return self.lowestCommonAncestor(root, q, p)
        # Nodes are in diff subtrees, so we can't get closer.
        if p.val <= root.val <= q.val:
            return root
        # Both in the left side.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Both in the right side.
        if q.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestorV2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Swap so that p.val <= q.val.
        if q.val < p.val: 
            return self.lowestCommonAncestorV2(root, q, p)

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr: 
                if p.val <= curr.val <= q.val:
                    return curr
                if p.val < curr.val and q.val < curr.val:
                    stack.append(curr.left)
                if p.val > curr.val and q.val > curr.val:
                    stack.append(curr.right)

        assert False, 'No solution found!'
