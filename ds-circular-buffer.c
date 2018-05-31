/*
    Circular buffers are fixed-size arrays that wrap around. They implement a queue
    efficiently because pops do not require the data to be shifted forward, instead
    we only shift the "position" of the circular buffer.

    Overwriting circular buffers (i.e. ones that replace the oldest element if
    something is pushed when it is full) are sometimes used in streaming applications
    where old data is not needed.
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 4

typedef struct _circ_buffer_t {
    size_t length;
    size_t position;
    int* data;
} circ_buffer_t;

// the "wraparound" function
size_t _clamp(size_t index) {
    return index & (SIZE - 1);
}

void check_mem(void* data) {
    if (!data) {
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(1);
    }
}

circ_buffer_t* circ_buffer_init() {
    circ_buffer_t* buffer = malloc(sizeof(circ_buffer_t));
    check_mem(buffer);

    int* data = malloc(SIZE * sizeof(int));
    check_mem(data);

    buffer->data = data;
    buffer->length = buffer->position = 0;

    return buffer;
}

void circ_buffer_free(circ_buffer_t* buffer) {
    free(buffer->data);
    free(buffer);
}

void circ_buffer_push(circ_buffer_t* buffer, int data) {
    if (buffer->length == SIZE) {
        fprintf(stderr, "Pushing a full buffer!\n");
        exit(1);
    }

    buffer->data[_clamp(buffer->position + buffer->length)] = data;
    buffer->length++;
}

int circ_buffer_pop(circ_buffer_t* buffer) {
    if (buffer->length == 0) {
        fprintf(stderr, "Popping an empty buffer!\n");
        exit(1);
    }

    int data = buffer->data[buffer->position];
    buffer->position = _clamp(buffer->position + 1);
    buffer->length--;

    return data;
}
