# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and false
# otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # An empty tree is a subtree of every tree.
            return True
        # If the subroot is not empty, but the root is empty, it's false.
        if not root: 
            return False
        if self.isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q: 
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtreeV2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_merkle = dict() 
        self.fillMerkleHashes(root, root_merkle)
        target_hash = self.fillMerkleHashes(subRoot, dict())

        for merkle in root_merkle.values(): 
            if target_hash == merkle:
                return True

        return False

    def fillMerkleHashes(self, root, merkle_dict): 
        if not root:
            return None
        merkle_dict[root] = f"#{root.val} {self.fillMerkleHashes(root.left, merkle_dict)} {self.fillMerkleHashes(root.right, merkle_dict)}"
        return merkle_dict[root]
