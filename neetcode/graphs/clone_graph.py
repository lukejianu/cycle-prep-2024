class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clones = {}

        def cloneNode(curr): 
            if curr.val in clones:
                return clones[curr.val]
            clone = Node(curr.val)
            clones[curr.val] = clone
            clone.neighbors = [cloneNode(neighbor) for neighbor in curr.neighbors]
            return clone

        return cloneNode(node) if node else None

