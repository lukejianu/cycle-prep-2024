# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.

class Codec:
    NONE_CHAR = 'N'
    def serialize(self, root):
        return ','.join(self.serializeHelper(root))

    def serializeHelper(self, root):
        if not root:
            return [self.NONE_CHAR]

        return [str(root.val)] + \
                self.serializeHelper(root.left) + \
                self.serializeHelper(root.right)
        
    def deserialize(self, data):
        return self.deserializeHelper(data.split(','), 0)[0]

    def deserializeHelper(self, data, i):
        if i >= len(data) or data[i] == self.NONE_CHAR: 
            return [None, i + 1]

        left, new_i = self.deserializeHelper(data, i + 1)
        right, new_new_i = self.deserializeHelper(data, new_i)

        return [TreeNode(data[i], left, right), new_new_i]
