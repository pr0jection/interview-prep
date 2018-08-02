'''
    The algorithm for finding the least common ancestor is similar to a tree
    search. If one of the nodes is on the left subtree and one is on the
    right subtree, we know that the root is the least common ancestor. But if
    both nodes lie on one subtree, we know that the least common ancestor
    will also be on that subtree.
'''

def least_common_ancestor(root, a, b):
    if not root:
        return None

    if root == a:
        return a

    if root == b:
        return b

    left = least_common_ancestor(root.left, a, b)
    right = least_common_ancestor(root.right, a, b)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right

    return None
