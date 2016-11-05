'''
    A fairly simple algorithm, the only thing we have to pay
    attention to are the recursive parameters and the stopping
    conditions.

    We must add or subtract one from the midpoint not only
    because we no longer wish to consider the midpoint a valid
    index, but because we'd loop infinitely otherwise:

        bs([1, 2], 0, 0, 1) => mid = 0
        bs([1, 2], 0, 0, 0) => mid = 0
        bs([1, 2], 0, 0, 0) => ...

    The stopping conditions stem from this fact. Although a
    search where (a == b) is valid (e.g. a list with 1 element),
    we must stop when the range is less than 0.
'''
blah = [1,4, 6,7,10,11]
def binary_search(xs, x, a, b):
    if not xs or a > b:
        return None

    mid = (a + b) / 2

    if xs[mid] == x:
        return x
    elif xs[mid] > x:
        return binary_search(xs, x, a, mid - 1)
    else:
        return binary_search(xs, x, mid + 1, b)
