symbols = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
]

symbols_inverse = { s: i for i, s in enumerate(symbols) }


def base_n_to_dec(num: str, base: int) -> int:
    '''
    A base 10 integer can be represented in any other base as
    a sum of the following form:

        x = (c0 * b**0) + (c1 * b**1) + (c2 * b**2) + ...

    So 5 in base 2 would be (1 * 2**0) + (0 * 2**1) + (1 * 2**2),
    or '101'. Each coefficient in the sum corresponds to one symbol
    or place in its representation.

    To convert any base to base 10, we decompose the representation
    as per the above formula, and convert the coefficient to its
    base 10 representation.
    '''

    res = 0
    for i, n in enumerate(reversed(num)):
        res += symbols_inverse[n] * (base ** i)
    return res


def dec_to_base_n(num: int, base: int) -> str:
    '''
    To convert base 10 to any other base, we do the inverse operation
    of the above, which amounts to finding the coefficients for each
    term in the sum.

    Starting in the ones place, or the first term in the sum, we
    obtain the digit by taking `n % b`, mapping it to a higher base
    (if the digit is > 9), then shifting the entire number over a place
    by taking `n / b`.
    '''

    res = []
    while num:
        res.append(symbols[num % base])
        num = int(num / base)
    return ''.join(reversed(res))
