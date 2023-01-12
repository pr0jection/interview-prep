"""
A least-recently-used cache eviction policy evicts values that were not read
or written to recently. A common way to implement this is to have a doubly- 
linked list and a hash map.

The linked list keeps elements in order of their usage (first = least recently
used, last = most recently used). By keeping a pointer to the start and to the
end of the list, we get O(1) insertions.

The hashmap provides O(1) random access to the cache, which we don't have with
just the linked list.
"""

from typing import Generic, Optional, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class LRUCache(Generic[K, V]):

    class Node(Generic[K, V]):
        def __init__(self, key: K, value: V) -> None:
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, size: int) -> None:
        self.size = size
        self.lookup = {}
        self.first = None
        self.last = None

    def _insert_node_at_end(self, new_node: Node[K, V]) -> None:
        if self.lookup:
            # insertion into a non-empty list
            self.last.next = new_node
            new_node.prev = self.last
            new_node.next = None
            self.last = new_node
        else:
            # insertion into an empty list (first insertion)
            self.first = new_node
            self.last = new_node

    def _move_node_to_end(self, existing_node: Node[K, V]) -> None:
        # if there's only 1 node, it's already at the end
        if len(self.lookup) > 1:
            if self.first == existing_node:
                self.first = existing_node.next
            else:
                existing_node.prev.next = existing_node.next

            if self.last == existing_node:
                self.last = existing_node.prev
            else:
                existing_node.next.prev = existing_node.prev

            self._insert_node_at_end(existing_node)

    def insert(self, key: K, value: V) -> None:
        existing = self.lookup.get(key)

        if existing:
            # if we're overwriting a key, make sure to handle the existing node
            existing.value = value
            self._move_node_to_end(existing)
        else:
            node = LRUCache.Node(key, value)

            if len(self.lookup) < self.size:
                # cache is not full yet, so we can just insert at the end
                self._insert_node_at_end(node)
            else:
                # cache is full, so we need to delete the least recently used node
                lru = self.first
                self.first = lru.next
                self._insert_node_at_end(node)
                del self.lookup[lru.key]

            self.lookup[key] = node

    def get(self, key: K) -> Optional[V]:
        node = self.lookup.get(key)
        if not node:
            return None

        # record the fact that it was used recently
        self._move_node_to_end(node) 
        return node.value
