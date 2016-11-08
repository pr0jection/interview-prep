#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define LAST_4_BITS (0xF)

/*
    There are several ways to calculate the population count. The fastest
    would probably be the processor's native POPCNT instruction.

    The second fastest is a variation of this lookup method, extended to
    16-bit numbers instead of 4-bit ones. The tradeoff is the extra space used.

    There is a general-purpose solution that gets every other bit from X, shifts
    by one to get every other other bit from X, and adds them together to get the
    number of ones for every 2-bit slice of X. Then it takes this value and repeats
    with different shifts/masks to do this for every 4-bit slice of X, 8-bit, etc.

    A slightly easier to understand algorithm that works well if there are more
    zeroes in the number is counting how many times (x &= x - 1) can be performed
    while x > 0. Note that if the LSB of x is 1, it will get cleared out by
    (x & x - 1), and if it is zero, the MSB will be cleared out by (x & x - 1). So
    at each step the number of bits set in x decreases by 1 until it is zero.
*/
uint32_t popcnt_lookup[16] = {
    0, 1, 1, 2,
    1, 2, 2, 3,
    1, 2, 2, 3,
    2, 3, 3, 4
};

uint32_t population_count(uint32_t number) {
    uint32_t count = 0;

    while (number) {
        count += popcnt_lookup[number & LAST_4_BITS];
        number >>= 4;
    }

    return count;
}

/*
    A number is a power of two if its binary representation consists of just
    one set bit. Alternatively, we can use the last method mentioned above,
    that always removes 1 bit from the number. If the result is 0, there was only
    one bit set (or it was already 0).
*/
bool is_power_of_two(uint32_t number) {
    return population_count(number) == 1;
}

/*

    Similarly to above, there exist native processor instructions to calculate the
    number of leading zeroes (CLZ). This method essentially performs a binary
    search for the first set bit, and is optimized by including a lookup table
    for when x is below a particular threshold (the lookup table, as above, can
    be extended further for faster computation.

    There exists a possibly more efficient algorithm for this specific problem (not
    CLZ in general) that works by repeatedly shifting the number right by 1, 2, 4, ...
    and bitwise OR'ing the number with the result, such that the highest set bit is
    propagated to all the lower bits, and adding one should produce a power of two.
*/
uint32_t clz_lookup[16] = {
    0, 1, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    4, 4, 4, 4
};

uint32_t next_power_of_two(uint32_t number) {
    uint32_t count = 0;

    if (number & 0xFFFF0000) { count += 16; number >>= 16; }
    if (number & 0xFF00) { count += 8; number >>= 8; }
    if (number & 0xF0) { count += 4; number >>= 4; }

    return 1 << (count + clz_lookup[number]);
}
