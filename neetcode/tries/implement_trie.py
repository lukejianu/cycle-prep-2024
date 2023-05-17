# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are various
# applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# - Trie() 
#   Initializes the trie object.
# - void insert(String word) 
#   Inserts the string word into the trie.
# - boolean search(String word) 
#   Returns true if the string word is in the trie (i.e., was inserted before), 
#   and false otherwise.
# - boolean startsWith(String prefix)
#   Returns true if there is a previously inserted string word that has the
#   prefix prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.characters = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            curr = curr.characters[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return True
