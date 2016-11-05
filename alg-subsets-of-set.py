'''
    Note that the cardinality of a set of subsets is 2^n, where n
    is the number of elements in the original set. This is in fact
    similar to the problem of enumerating all n-bit numbers: for
    each bit or element, we must make the decision to include it
    (setting the bit to 1) or exclude it (setting the bit to 0).

    This suggests an easy recursive solution: for each element in
    the set of subsets for an original set of size n - 1, we can
    either prepend the subset with the new element, or not.
'''

def subsets_of_set(xs):
    if not xs:
        return [[]]

    singleton = xs[0]
    rest = subsets_of_set(xs[1:])
    result = []

    for r in rest:
        result.append(r)
        result.append([singleton] + r)

    return result
