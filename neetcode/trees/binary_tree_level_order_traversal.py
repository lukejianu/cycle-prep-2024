# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        levels = []
        while queue: 
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                curr = queue.pop()
                level.append(curr.val)
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            levels.append(level)
        
        return levels

    def levelOrderV2(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.levelOrderHelper(root, 0, levels)
        return levels
         
    def levelOrderHelper(self, root, level, levels):
        if not root:
            return None 
        if level == len(levels): 
            levels.append([])
        levels[level].append(root.val)
        self.levelOrderHelper(root.left, level + 1, levels)
        self.levelOrderHelper(root.right, level + 1, levels)

