/*
    Bloom filters are a simple probabilistic data structure implementing
    a set (though removals are not possible). The membership check
    effectively returns "possibly in set" or "definitely not in set,"
    depending on:

        (1) the number of bits used for the bloom filter
        (2) the number of hash functions, as well as their distribution
        (3) the number of elements already in the bloom filter.

    The advantage of a bloom filter is its memory footprint. It is also
    unique in that the time for the add/is_member functions remains
    constant despite the amount of elements already in the set.

    Sometimes bloom filters are used as a low-memory "first pass" to
    avoid running expensive computations (which only happen if an element
    is "possibly" in the set).
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int32_t bloom_filter_t;

int32_t hash1(int32_t val) {
    val = ~val + (val << 15);
    val = val ^ (val >> 12);
    val = val + (val << 2);
    val = val ^ (val >> 4);
    val = val * 2057;
    val = val ^ (val >> 16);
    return val;
}


int32_t hash2(int32_t val) {
    int c = 0x27d4eb2d;
    val = (val ^ 61) ^ (val >> 16);
    val = val + (val << 3);
    val = val ^ (val >> 4);
    val = val * c;
    val = val ^ (val >> 15);
    return val;
}


bloom_filter_t bf_init() {
    return 0;
}


void bf_add(bloom_filter_t* bf, int32_t val) {
    int h1 = hash1(val) % 32;
    int h2 = hash2(val) % 32;
    *bf = *bf | (1 << h1) | (1 << h2);
}


bool bf_is_member(bloom_filter_t* bf, int32_t val) {
    int h1 = hash1(val) % 32;
    int h2 = hash2(val) % 32;
    bloom_filter_t u = *bf;
    return (u & (1 << h1)) && (u & (1 << h2));
}
