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
