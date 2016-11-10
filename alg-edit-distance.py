'''
    Edit distance (here, implemented as Levenshtein distance) is a measure of
    how dissimilar two strings are. We may transform a target string into a
    source string by either deleting a letter from the target string, inserting
    a letter into the target string, or replacing a letter with another letter
    in the target string. The cost of these operations in this implementation is
    constant (i.e. we add 1 to each operation) but it need not be. The algorithm
    is basically trying each of these operations at each step (point in the
    strings) and returning the minimum cost.
'''


def top_down_edit_distance(a, b):
    # if one of the strings is empty, the operations must all be
    # insertions or deletions
    if not a:
        return len(b)

    if not b:
        return len(a)

    # if the first letters are the same, it is optimal to just
    # ignore them since the cost of an operation now and the cost
    # of an operation later would be the same
    if a[0] == b[0]:
        return top_down_edit_distance(a[1:], b[1:])

    # deletion: remove a letter from the target string
    deletion = top_down_edit_distance(a, b[1:])

    # insertion: insert the first letter of the source string
    # into the target string
    insertion = top_down_edit_distance(a[1:], b)

    # replacement: replace the first letter of the target string with
    # the first letter of the source string
    replacement = top_down_edit_distance(a[1:], b[1:])

    return 1 + min([deletion, insertion, replacement])


def bottom_up_edit_distance(a, b):
    table = []

    for i in range(len(a)):
        table.append([0] * len(b))

    # the first horizontal and vertical rows are constant
    # since the only thing you can do is insert/delete
    for i in range(len(a)):
        table[i][0] = i + 1

    for j in range(len(b)):
        table[0][j] = j + 1

    # the same algorithm as above, simply using already computer
    # values in the table instead of recursive calls
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                table[i][j] = table[i - 1][j - 1]
            else:
                deletion = table[i - 1][j]
                insertion = table[i][j - 1]
                replacement = table[i - 1][j - 1]

                table[i][j] = 1 + min([deletion, insertion, replacement])

    return table[len(a) - 1][len(b) - 1]
