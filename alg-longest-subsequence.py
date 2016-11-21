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
