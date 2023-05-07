"""
Taking the MOD of some hash function works poorly when load balancing or
sharding. Because servers may be added or removed, changing the "denominator"
would cause almost all mappings to be shifted. Given some N, N % x and N % y
only have `min(x, y) / gcd(x, y)` mappings in common.

In consistent hashing, most mappings remain the same. Only `k / n` mappings
must change, where k is the total number of keys and n is the number of nodes.

Two problems exist with the basic implementation:

 - Domino effect: if one server goes down, then all of its load is transferred
   to the next server, which may become overloaded and also go down, etc etc.

 - Depending on the hash algorithm, nodes may not be evenly distributed around
   the circle

A simple way to solve both is to add nodes to the ring multiple times.

"""

from bisect import bisect, bisect_left
from hashlib import sha256
from typing import Any


class ConsistentHash:
    def __init__(self) -> None:
        # this is a sorted list which enables binary search, however
        # it should probably be a self-balancing binary search tree,
        # so that additions and removals of nodes are O(log n) rather
        # than O(n)
        self.keys = []
        self.key_to_node = {}
        self.total_slots = 64

    def _hash(self, s: str) -> int:
        h = sha256()
        h.update(bytes(s, encoding="utf8"))
        return int(h.hexdigest(), 16) % self.total_slots

    def add_node(self, node: str) -> None:
        if len(self.keys) == self.total_slots:
            raise Exception("Ring is full")

        key = self._hash(node)
        idx = bisect(self.keys, key)

        self.keys.insert(idx, key)
        self.key_to_node[key] = node

    def remove_node(self, node: str) -> None:
        key = self._hash(node)
        # bisect_left to find the value if it exists
        idx = bisect_left(self.keys, key)

        if idx == len(self.keys) or self.keys[idx] != key:
            raise Exception("Node does not exist")

        self.keys.pop(idx)
        del self.key_to_node[key]

    def assign(self, identifier: str) -> str:
        key = self._hash(identifier)
        # find the first node to the right of this key
        # if it's at the end of the array, loop back to 0
        idx = bisect(self.keys, key) % len(self.keys)

        return self.key_to_node[self.keys[idx]]
