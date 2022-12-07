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


def edit_distance(a, b):
    table = []

    # build a table representing "how many edits are needed
    # to get from a[:i] to b[:j]"
    for i in range(len(a) + 1):
        table.append([0] * (len(b) + 1))

    # the first horizontal and vertical rows are constant
    # since the only thing you can do is insert/delete
    for i in range(len(a) + 1):
        table[i][0] = i

    for j in range(len(b) + 1):
        table[0][j] = j

    # note the table is effectively 1-indexed because it tracks
    # "prefix up to an index" (the 0'th prefix is an empty string)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # if the last letters are the same, no edits are necessary
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                deletion = table[i - 1][j]
                insertion = table[i][j - 1]
                replacement = table[i - 1][j - 1]

                table[i][j] = 1 + min([deletion, insertion, replacement])

    return table[len(a)][len(b)]
