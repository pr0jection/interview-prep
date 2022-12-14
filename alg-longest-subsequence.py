def longest_increasing_subsequence(xs):
    if not xs:
        return 0

    # table[n] represents the longest increasing subsequence
    # that ends with the element xs[n]. thus the LIS for a
    # subsequence that ends at the first element is just 1
    table = [1]

    for i in range(1, len(xs)):
        # we can always just have a subsequence of just this element
        best = 1

        # loop over the longest increasing subsequences ending at
        # previous elements. maximize the value among those whose
        # element is less than the current element
        for j in range(0, i):
            if xs[j] < xs[i]:
                candidate = table[j] + 1

                if candidate > best:
                    best = candidate

        table.append(best)

    # we're still not sure exactly which element we want to end at.
    # just take the max of all possibilities
    return max(table)


'''
    This bottom-up approach is similar to the one taken in other string DP problems,
    namely we define the table's indices by the ending indices of the strings.
'''
def longest_common_subsequence(xs, ys):
    if not xs or not ys:
        return 0

    # build a table representing the longest common subsequence
    # of xs[:i] and ys[:j]
    table = []

    for i in range(len(xs) + 1):
        table.append([0] * (len(ys) + 1))

    # note the table is effectively 1-indexed because it tracks
    # "up to an index" (up to the 0'th index is an empty string)
    for i in range(1, len(xs) + 1):
        for j in range(1, len(ys) + 1):
            # if the strings contain the same character at the end,
            # we know it is ALWAYS part of the optimal solution
            if xs[i - 1] == ys[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            # otherwise, ignore this letter and take the best surrounding solution
            else:
                table[i][j] = max([table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]])

    return table[len(xs)][len(ys)]
