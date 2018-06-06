'''
    A trie is a kind of search tree that can implement a set or associative
    array. A node represents a common prefix of its descendents, the
    complete value is a path from the root to some node marked as a
    final value (perhaps a leaf). This marker is True/False in this
    implementation, but could alternatively be a value if we were implementing
    an associative array.

    Because tries are a tree of prefixes, they are typically used to store
    strings or bitsets. They can be used to implement predictive text/autocomplete.

    This implementation optimizes (slightly) for space over performance. It's
    possible, instead of using a linked list, to store children as a fixed-size
    array with the number of elements being the size of the alphabet.
'''

class TrieNode(object):
    def __init__(self, char):
        self.value = char
        self.terminator = False
        self.children = []


def trie_init():
    return TrieNode('')


def trie_insert(node, string):
    if not string:
        node.terminator = True
        return

    letter = string[0]
    letter_node = None

    for child in node.children:
        if child.value == letter:
            letter_node = child
            break

    if not letter_node:
        letter_node = TrieNode(letter)
        node.children.append(letter_node)

    trie_insert(letter_node, string[1:])


def trie_find(node, string):
    if not string:
        return node.terminator

    letter = string[0]

    for child in node.children:
        if child.value == letter:
            return trie_find(child, string[1:])

    return False
