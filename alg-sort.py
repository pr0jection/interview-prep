'''
    Intuitively, quick-sort works by choosing a pivot element
    (any element works, usually it's the last one in the list for
    ease of implementation or a random index), then arranging the
    list in two parts, one with all the elements less than the
    pivot and one with all the elements greater than the pivot. Then
    quick-sort is recursively called to sort these elements.

    The worst case running-time for quick-sort is O(n^2) -- imagine
    if the pivot element was always chosen to be the least or
    greatest element, then we'd have to make n calls of size n - 1,
    n - 2, etc.

    This implementation is in-place but not stable. In theory you
    could make it stable but not in-place if you kept separate lists
    and appended to them in a left-to-right iteration of xs.
'''
def quick_sort(xs, a, b):
    if a >= b:
        return

    def swap(i, j):
        tmp = xs[i]
        xs[i] = xs[j]
        xs[j] = tmp

    def partition():
        # choose the pivot as the last element
        pivot = xs[b]
        i = a

        # move all the elements less than the pivot
        # to the left side of the list
        for j in range(a, b):
            if xs[j] < pivot:
                swap(i, j)
                i = i + 1

        # i is now the position of the split, swap it
        # with the pivot and return
        swap(i, b)
        return i

    pivot_idx = partition()

    # recursively sort the two sides of the list
    quick_sort(xs, a, pivot_idx - 1)
    quick_sort(xs, pivot_idx + 1, b)


'''
    Merge-sort works by de-constructing the lists into smaller parts,
    sorting each part, then merging the results into the final result.

    It can be used to sort items that are too large to fit in memory. For
    example, you can start reading records from machine 1, writing two-record
    sublists alternately to machine 3 and 4. Then you can merge the two-record
    sublists into four-record sublists writing to machine 1 and 2, repeating
    until you get one list with all the data.

    Merge-sort works in O(n log n) worst case time, but requires O(n)
    additional space (that is, it is not done in place). Typical implementations
    are stable.
'''

def merge_sort(xs):
    if len(xs) < 2:
        return xs

    mid = len(xs) / 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])

    result = []
    i = 0
    j = 0

    # merge two recursively sorted sublists by comparing minimum elements
    while i < len(left) or j < len(right):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


'''
    Topological sort is a sort of a directed (acyclic) graph such that all for all
    edges a -> b, a comes before b in the sorted result. The algorithm follows from
    this definition: we can look at all nodes who never appear on the RHS (i.e. don't
    have incoming edges) since they would always be safe to place in the front of the
    list. Note that we could select any node with no incoming edges, meaning the
    solution is not unique. It runs in O( V + E ).
'''
def topological_sort(graph):
    result = []
    incoming_edges = {}
    no_incoming_edges = set()

    # build a base set for nodes with no incoming edges
    for e in graph.incoming_edges:
        incoming_edges[e] = len(graph.incoming_edges[e])

        if not incoming_edges[e]:
            no_incoming_edges.add(e)

    # graph is cyclic
    if not no_incoming_edges:
        return None

    while no_incoming_edges:
        some_edge = no_incoming_edges.pop()
        result.append(some_edge)

        # a node with no incoming edges can always be added to the
        # result set without violating constraints. then, update the
        # remaining counts to exclude this node
        for e in graph.outgoing_edges[some_edge]:
            incoming_edges[e] = incoming_edges[e] - 1

            if not incoming_edges[e]:
                no_incoming_edges.add(e)

    # graph contains a cycle
    if [ k for k, v in incoming_edges.items() if v ]:
        return None

    return result


'''
    Radix sort is a non-comparative sorting algorithm that works by looking at each
    digit (10's place) in a number, assigning it to a bucket based off it, and
    concatenating the buckets. When the number of digits in any number is fixed (e.g.
    sorting 000-999) this can achieve a lower upper bound than the minimum for
    comparison-based sorts -- O(n) instead of O(n log n). For integers, we start at
    the least significant digit (a most significant digit sort would result in
    lexographic order, perhaps useful for strings). At each step we preserve the
    order of the original array, so radix sort is stable.
'''
def radix_sort(xs):
    l = len(str(max(xs))) # how many buckets

    for i in range(l):
        buckets = [ [] for _ in range(10) ]

        for n in xs:
            digit = (n // (10 ** i)) % 10
            buckets[digit].append(n)

        xs = [ n for bucket in buckets for n in bucket ]

    return xs
