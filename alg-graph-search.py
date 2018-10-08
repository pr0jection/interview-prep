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

'''
    Depth-first search can also be used to find cycles in a graph.
    The undirected case is easy: if you encounter a node that you
    have previously seen in your search, there is a cycle.

    For a directed graph, we need to find the presence of any
    back-edges, or edges pointing back to another node in the
    current path. We can do this by looking at the current stack.
'''

import sys

from Queue import Queue

class UndirectedGraph(object):
    def __init__(self):
        self.edges = {}

    def add_node(self, a):
        self.edges[a] = []

    def add_edge(self, a, b, weight=None):
        self.edges[a].append((b, weight))
        self.edges[b].append((a, weight))

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


'''
    Dijkstra's algorithm is a fairly intuitive graph search algorithm to compute
    single-source shortest path (all shortest paths from a root). We basically have
    a set of all vertices and weights (initially 0 for the root, infinity for the rest),
    and repeatedly pop the vertex with the lowest weight. We can iterate over its
    neighbors and update their weights if lowest_weight_to_point + weight_to_neighbor
    is lower than the currently best seen weight. Popping the vertex with the lowest
    weight is the key to making this work, since we know (assuming non-negative weights)
    that minimum weight is the final shortest weight to that node.

    This algorithm runs in O( E + V^2 ) time, and since E = O(V^2) generally just
    O(V^2). If we use a min heap for finding the minimum weight, we can take this
    down to O( E + V log V ).
'''
def dijkstras_algorithm(graph, root):
    nodes = set(graph.edges.keys())
    shortest = { root: 0 }

    while nodes:
        min_node = None
        min_weight = None

        for node in shortest:
            if node in nodes and (not min_weight or shortest[node] < min_weight):
                min_node = node
                min_weight = shortest[node]

        nodes.remove(min_node)

        for neighbor, weight in graph.get_edges(min_node):
            if neighbor not in shortest or shortest[neighbor] > min_weight + weight:
                shortest[neighbor] = min_weight + weight

    return shortest

'''
    The Floyd-Warshall algorithm for solving the all-pairs shortest path problem works
    by considering the paths that go through an intermediate node (for every pair that's
    not an edge, there is at least 1 intermediate node), for all possible intermediate
    nodes. If a path going from i to k then k to j is faster than the previously best seen
    path going from i to j, then update its distance.

    It runs in O(V^3) time.
'''
def floyd_warshall_algorithm(graph):
    nodes = set(graph.edges.keys())

    distances = {}

    # transform edges dict into a dict of dicts
    for source, (destination, weight) in graph.edges.iteritems():
        if source not in distances:
            distances[source] = {}

        distances[source][destination] = weight

    for source in nodes:
        distances[source][source] = 0

    for k in nodes:
        for i in nodes:
            for j in nodes:
                direct = distances[i].get(j, sys.maxint)
                intermediate1 = distances[i].get(k, sys.maxint)
                intermediate2 = distances[k].get(j, sys.maxint)

                if direct > intermediate1 + intermediate2:
                    distances[i][j] = intermediate1 + intermediate2

    return distances
