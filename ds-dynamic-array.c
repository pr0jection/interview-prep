/*
    Dynamic arrays are sort of like a hybrid between regular arrays
    and linked lists, providing O(1) random access with good cache
    performance, O(1) amortized appending, and O(1) popping.

    Appending is amortized O(1) because we must have paid off
    each O(n) resize with n insertions beforehand.

    On the other hand, insertion and deletion at arbitrary indexes
    is O(n). Technically this is the same for linked lists, although
    linked lists do this in constant time if performed during iteration.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_MAX 8

typedef struct _dyn_array_t {
    size_t size;
    size_t max;
    int* data;
} dyn_array_t;

void check_mem(void* data) {
    if (!data) {
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(1);
    }
}

dyn_array_t* dyn_array_init() {
    dyn_array_t* array = malloc(sizeof(dyn_array_t));
    check_mem(array);

    int* data = malloc(INITIAL_MAX * sizeof(int));
    check_mem(data);

    array->size = 0;
    array->max = INITIAL_MAX;
    array->data = data;

    return array;
}

void dyn_array_free(dyn_array_t* array) {
    free(array->data);
    free(array);
}

int dyn_array_read(dyn_array_t* array, size_t index) {
    return array->data[index];
}

void dyn_array_append(dyn_array_t* array, int datum) {
    if (array->size == array->max) {
        size_t new_max = array->max << 1;

        int* new_data = malloc(new_max * sizeof(int));
        check_mem(new_data);

        memcpy(new_data, array->data, sizeof(int) * array->size);
        free(array->data);

        array->data = new_data;
        array->max = new_max;
    }

    array->data[array->size] = datum;
    array->size++;
}

int dyn_array_pop(dyn_array_t* array) {
    if (array->size == 0) {
        fprintf(stderr, "Popping an empty array!\n");
        exit(1);
    }

    array->size--;
    return array->data[array->size];
}
