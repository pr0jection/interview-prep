def binary_search(xs, x, a, b):
    if not xs or a > b:
        return None

    mid = (a + b) / 2

    if xs[mid] == x:
        return x
    elif xs[mid] > x:
        return binary_search(xs, x, a, b - 1)
    else:
        return binary_search(xs, x, a + 1, b)
