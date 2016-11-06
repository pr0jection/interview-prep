'''
    Breadth- and depth-first search are very similar algorithms,
    the primary difference is in the data structure used to store
    the nodes to be visited. Breadth-first search uses a FIFO queue,
    meaning we visit an entire "level" before proceeding to the next
    "level" (which would be added to the back of the queue). The
    depth-first search uses a stack instead, which reverses this
    operation (the most recently visited node is processed again,
    meaning we continually move down its neighbors).

    The only other difference is an optimization in the breadth-first
    search: we add adjacent nodes to the visited set before actually
    processing them. This helps us not have any duplicates stored in
    the queue itself. It is incorrect to do this for depth-first
    search, however:

        A--B--E
        |  |
        C--D

    If we started from A, we'd add B and C to the visited set, and
    prevent the correct depth-first execution A-B-D-C from occuring.

    Note that the stack used by the depth-first search may be made
    implicit via the call-stack, allowing us to easily translate the
    algorithm into a recursive variant.
'''

from Queue import Queue

class UndirectedGraph(object):
    def __init__(self):
        self.edges = {}

    def add_node(self, a):
        self.edges[a] = []

    def add_edge(self, a, b):
        self.edges[a].append(b)
        self.edges[b].append(a)

    def get_edges(self, a):
        return self.edges[a]


def breadth_first_search(graph, root, predicate):
    nodes = Queue()
    nodes.put(root)
    visited = set([root])

    while nodes.qsize() > 0:
        node = nodes.get()

        if predicate(node):
            return node

        for adjacent in graph.get_edges(node):
            if adjacent not in visited:
                nodes.put(adjacent)
                visited.add(adjacent)

    return None


def depth_first_search(graph, root, predicate):
    nodes = [root]
    visited = set()

    while nodes:
        node = nodes.pop()
        visited.add(node)

        if predicate(node):
            return node

        for adjacent in graph.get_edges(node):
            if adjacent not in visited:
                nodes.append(adjacent)

    return None
