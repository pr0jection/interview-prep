'''
    The key insight is that a linked list for a forward sequence
    is constructed backwards, i.e.

        1 : (2 : (3 : (4 : (5 : Nil) ) ) )

    In a strictly evaluated language, the innermost list (5 : Nil)
    must be evaluated first. This suggests that to construct a
    reverse list, we must first evaluate (1 : Nil), then (2 : ...)
    and so forth. This evaluation order is exactly what we get
    when iterating over the original list forwards, so we can simply
    prepend the elements as we go.
'''

class Node(object):
    def __init__(self, value, right=None):
        self.value = value
        self.right = right


def reverse_iterative(node):
    rev = None

    while node:
        rev = Node(node.value, rev)
        node = node.right

    return rev


def reverse_inplace(node):
    prev = None

    while node:
        tmp = node.right
        node.right = prev
        prev = node
        node = tmp


# probably cheating by using an accumulator but eh
def reverse_recursive(node, rev=None):
    if not node:
        return rev

    return reverse_recursive(node.right, Node(node.value, rev))
