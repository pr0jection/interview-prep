/*
    Heaps are data structures optimized for minimum (or maximum) element
    access, providing O(1) peeking and O(log N) insertion/deletion/popping.
    Heaps are said to satisfy the heap property: the children of a node
    are always greater (or less) than or equal to the parent node. Heaps
    can be used to implement priority queues (and thus valuable in particular
    graph algorithms) or heapsort.

    This particular implementation is a binary min heap with a fixed size.
    It should be fairly trivial to extend this implementation to use a dynamic
    array.

    There are many varieties of heaps, primarily differing in their tree
    structure. A Fibonacci heap, for example, uses a collection of trees
    to provide amortized O(1) insertions and merges.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_FIXED_SIZE (10)
#define SUCCESS (0)
#define EMPTY_HEAP (-1)
#define FULL_HEAP (-2)

#define INT_SWAP(a, b) do { int tmp = a; a = b; b = tmp; } while (0)

struct heap_t {
    size_t size;
    int data[MAX_FIXED_SIZE];
};

struct heap_t* heap_init() {
    struct heap_t* heap = malloc(sizeof(struct heap_t));

    if (!heap) {
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(1);
    }

    // technically not portable but whatever
    memset(heap, 0, sizeof(struct heap_t));
    return heap;
}

void heap_free(struct heap_t* heap) {
    free(heap);
}

int heap_insert(struct heap_t* heap, int value) {
    if (heap->size == MAX_FIXED_SIZE) {
        return FULL_HEAP;
    }

    size_t n = heap->size;

    heap->data[n] = value;
    heap->size++;

    while (n > 0) {
        size_t parent = (n - 1) / 2;

        if (heap->data[n] < heap->data[parent]) {
            INT_SWAP(heap->data[n], heap->data[parent]);
        } else {
            break;
        }

        n = parent;
    }

    return SUCCESS;
}

int heap_peek(struct heap_t* heap, int* ret) {
    if (heap->size == 0) {
        return EMPTY_HEAP;
    }

    *ret = heap->data[0];
    return SUCCESS;
}

int heap_pop(struct heap_t* heap, int* ret) {
    if (heap->size == 0) {
        return EMPTY_HEAP;
    }

    *ret = heap->data[0];

    heap->size--;
    heap->data[0] = heap->data[heap->size];

    size_t n = 0;

    // while there is at least a left child
    while ((2 * n) + 1 < heap->size) {
        size_t left_child_index = (2 * n) + 1;
        size_t right_child_index = (2 * n) + 2;

        size_t min_child_index = left_child_index;

        if (right_child_index < heap->size && heap->data[left_child_index] > heap->data[right_child_index]) {
            min_child_index = right_child_index;
        }

        if (heap->data[n] > heap->data[min_child_index]) {
            INT_SWAP(heap->data[n], heap->data[min_child_index]);
            n = min_child_index;
        } else {
            break;
        }
    }

    return SUCCESS;
}
