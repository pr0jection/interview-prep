import heapq

'''
    Given a list of integers, find the k highest-valued ones. This can be done naively by
    sorting the list and taking a fixed slice in O(n log n) time, but we can improve this
    down to O(n log k) by constructing a k-sized _min_ heap.

    The algorithm has the same intuition as finding a single max element in a list: start
    with the first element as the "min," and replace it with any larger elements found. Here,
    the min heap functions as a multi-dimensional "min" element, giving us the smallest
    element seen thus far so we can replace it upon encountering a bigger one.
'''

def max_k_integers(xs, k):
    min_heap = []

    for x in xs:
        if len(min_heap) < k:
            heapq.heappush(min_heap, x)
            continue

        if min_heap[0] < x:
            heapq.heapreplace(min_heap, x)

    return min_heap


'''
    Find the k'th (smallest) element in an unsorted list. This type of algorithm is called
    a selection algorithm, and this particular implementation is called quickselect. It is
    very similar to quicksort, except instead of recursing on both sublists it just selects
    the one which will contain the given index. The running time here is on average O(n)
    but O(n^2) in the worst case.

    Other solutions exist. We can naively sort and take the k'th element (n log n), or find 
    the min k elements and take the last one (n log k).
'''
def kth_element(xs, k, a, b):
    if a == b:
        return xs[a]

    def partition():
        pivot = xs[b]
        i = a

        for j in range(a, b):
            if xs[j] < pivot:
                xs[i], xs[j] = xs[j], xs[i]
                i += 1

        xs[b], xs[i] = xs[i], xs[b]
        return i

    pivot_idx = partition()

    if k == pivot_idx:
        return xs[k]
    elif k < pivot_idx:
        return kth_element(xs, k, a, pivot_idx - 1)
    else:
        return kth_element(xs, k, pivot_idx + 1, b)
