import sys

INFINITY = sys.maxint - 1

'''
    Prim's algorithm finds the minimum spanning tree for a graph. It does so
    by maintaining two separate sets of nodes: those already part of the MST
    and those not. At each step, we consider all the edges connecting the two
    sets and pick the edge with the minimum weight to include in the MST.

    The first node to go into the MST set can be arbitrary. The algorithm works
    by keeping track of the cheapest edge from each node. In subsequent iterations,
    we take the cheapest edge from the not-yet-included nodes, include it, and
    update the cheapest edges to the nodes connected to that one.
'''

def prims_algorithm(graph):
    included_nodes = set()
    excluded_nodes = set(graph.edges.keys())

    cheapest_cost = {}
    cheapest_edge = {}

    result = []

    while excluded_nodes:

        min_cost = sys.maxint
        min_node = None

        for node in excluded_nodes:
            cost = cheapest_cost(node, INFINITY)

            if cost < min_cost:
                min_cost = cost
                min_node = node

        excluded_nodes.remove(min_node)
        included_nodes.add(min_node)

        edge = cheapest_edge.get(min_node)

        if edge:
            result.append( (min_node, edge) )

        for destination, cost in graph.edges[min_node]:
            if destination in excluded_nodes and cost < cheapest_cost.get(destination, INFINITY):
                cheapest_cost[destination] = cost
                cheapest_edge[destination] = min_node

    return result
