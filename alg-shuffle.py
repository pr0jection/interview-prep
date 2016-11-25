import random

'''
    This shuffle works by choosing a random element from
    the remaining elements, and moving it to the back
    of the list where it won't be chosen again. Intuitively,
    this algorithm is picking one out of the n! possibilities
    of a shuffled sequence, or permutation (i.e. n * (n - 1)
    * (n - 2) * ...)
'''
def shuffle(xs):
    for i in range(len(xs) - 1, 0, -1):
        r = random.randint(0, i)
        xs[i], xs[r] = xs[r], xs[i]

    return xs
