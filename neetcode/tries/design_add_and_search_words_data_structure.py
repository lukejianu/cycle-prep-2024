# Design a data structure that supports adding new words and finding if a string
# matches any previously added string.

# Implement the WordDictionary class:

# - WordDictionary() 
#   Initializes the object.
# - void addWord(word)
#   Adds word to the data structure, it can be matched later.
# - bool search(word)
#   Returns true if there is any string in the data structure that matches word or
#   false otherwise. word may contain dots '.' where dots can be matched with any
#   letter.

class TrieNode: 
    def __init__(self):
        self.characters = dict()
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            curr = curr.characters[c]        
        curr.end = True

    def search(self, word: str) -> bool:

        # Determines if word[i:] is found starting at the given root node.
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)): 
                c = word[j] 
                # Since see a dot, our search splits off to try every child.
                if c == '.': 
                    for child in curr.characters.values(): 
                        if dfs(j + 1, child):
                            return True
                else:
                    if c not in curr.characters: 
                        return False
                curr = curr.characters[c]
            return curr.end

        return dfs(0, self.root)

