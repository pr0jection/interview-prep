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
