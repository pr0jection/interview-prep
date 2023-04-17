'''
    A trie is a kind of search tree that can implement a set or associative
    array. A node represents a common prefix of its descendents, the
    complete value is a path from the root to some node marked as a
    final value (perhaps a leaf). This marker is True/False in this
    implementation, but could alternatively be a value if we were implementing
    an associative array.

    Because tries are a tree of prefixes, they are typically used to store
    strings or bitsets. They can be used to implement predictive text/autocomplete.

    In a different language, you might choose to store children in a fixed-size
    array (with the number of elements being the size of the alphabet).
'''

class TrieNode:
    def __init__(self, char: str) -> None:
        self.value = char
        self.terminator = False
        self.children = {}

    def insert(self, string: str) -> None:
        if not string:
            self.terminator = True
            return

        letter = string[0]
        node = self.children.get(letter)

        if not node:
            node = TrieNode(letter)
            self.children[letter] = node

        node.insert(string[1:])

    def find(self, string: str) -> bool:
        if not string:
            return node.terminator

        node = self.children.get(string[0])
        if node:
            return node.find(string[1:)
        
        return False
        

trie = TrieNode('')
