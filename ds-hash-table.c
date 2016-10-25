/*
    Hash tables provide on average, amortized O(1) insertion and lookup.
    In the worst case scenario, where a hash function hashes each key
    to the same value, this may in fact be O(n).

    This implementation uses the separate chaining method to handle
    hash collisions. That is, if two keys map to the same bucket, a linked
    list is created and traversed to find or insert a value. Hash tables
    may very well use a data structure other than a linked list (like a tree
    or dynamic array) to perform separate chaining, or use an altogether
    different method of hash collision resolution. For example, open
    addressing tries to find a nearby open bucket if the one being hashed
    to is full. This has its own tradeoffs: there are no dynamic allocations
    and it can potentially save space for small elements, but the requirements
    of its hash function are more strict (e.g. it must have low clustering).

    This implementation also does not dynamically resize its number of buckets,
    and is thus slow when the number of entries is much higher than NUM_BUCKETS,
    and wastes space when the number is much lower. It could potentially resize
    itself after hitting a specific load factor (num entries / num buckets) by
    increasing the number of buckets and remapping its entries, while still
    achieving an amortized constant cost over insert/delete operations.

    Every hashed key that shares a common factor with the number of buckets will
    end up in a bucket that is a multiple of this factor. For example, if the
    number of buckets is 12, then

        keys 0, 12, 24, 36 => bucket 0
        keys 3, 15, 27, 39 => bucket 3
        keys 6, 18, 30, 42 => bucket 6

    If the distribution is uneven and tends to be multiples of 3, certain
    buckets will be more crowded than others. This is why we choose a prime
    number for the number of buckets -- it has very few common factors. If the
    distribution is fairly even (i.e. you are using a good hash function), this
    is less of a problem.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NUM_BUCKETS 7
#define STR_EQ(a, b) (!strcmp(a, b))

typedef struct _node_t {
    char* key;
    char* value;
    struct _node_t* next;
} node_t;

typedef struct _hash_table_t {
    node_t* buckets[NUM_BUCKETS];
} hash_table_t;

void* emalloc(size_t size) {
    void* data = malloc(size);

    if (!data) {
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(1);
    }

    return data;
}

hash_table_t* hash_table_init() {
    hash_table_t* table = emalloc(sizeof(hash_table_t));
    // technically not portable but whatever
    memset(table, 0, sizeof(hash_table_t));
    return table;
}

void hash_table_free(hash_table_t* table) {
    for (int i = 0; i < NUM_BUCKETS; i++) {
        node_t* node = table->buckets[i];

        while (node != NULL) {
            node_t* next = node->next;
            // we don't free the key/value strings which might create a leak
            free(node);
            node = next;
        }
    }
}

unsigned int hash_string(char* key) {
    unsigned int hash = 5381;
    int c;

    while ((c = *key++)) {
        hash = ((hash << 5) + hash) + c;
    }

    return hash;
}

void hash_table_put(hash_table_t* table, char* key, char* value) {
    unsigned int hash = hash_string(key) % NUM_BUCKETS;
    node_t* node = table->buckets[hash];

    node_t* new_node = emalloc(sizeof(node_t));
    new_node->key = key;
    new_node->value = value;
    new_node->next = NULL;

    if (node == NULL) {
        table->buckets[hash] = new_node;
    } else {
        while (1) {
            if (STR_EQ(node->key, key)) {
                node->value = value;
                break;
            } else if (node->next == NULL) {
                node->next = new_node;
                break;
            } else {
                node = node->next;
            }
        }
    }
}

char* hash_table_get(hash_table_t* table, char* key) {
    unsigned int hash = hash_string(key) % NUM_BUCKETS;
    node_t* node = table->buckets[hash];

    while (node != NULL) {
        if (STR_EQ(node->key, key)) {
            return node->value;
        } else {
            node = node->next;
        }
    }

    return NULL;
}

void hash_table_delete(hash_table_t* table, char* key) {
    unsigned int hash = hash_string(key) % NUM_BUCKETS;
    node_t* node = table->buckets[hash];
    node_t* prev = NULL;

    while (node != NULL) {
        if (STR_EQ(node->key, key)) {
            if (prev == NULL) {
                table->buckets[hash] = NULL;
            } else {
                prev->next = node->next;
            }

            free(node);
            node = NULL;
        } else {
            prev = node;
            node = node->next;
        }
    }
}
