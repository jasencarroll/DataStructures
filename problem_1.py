class Node:
    """A node in a doubly linked list"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__(self, capacity):
        """Initialize the LRU cache with a given capacity."""
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key -> node reference
        self.head = None  # Most recently used
        self.tail = None  # Least recently used
        self.size = 0     # Current size of the cache

    def _remove(self, node):
        """Removes a node from the doubly linked list."""
        if not node:
            return

        # If this node is the only node (head == tail)
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            # Update the head
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            # Update the tail
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            # Remove the node from between its neighbors
            node.prev.next = node.next
            node.next.prev = node.prev

        # Dereference the node
        node.prev = node.next = None

    def _add_to_head(self, node):
        """Adds a node to the head of the doubly linked list (most recently used)."""
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            # If the list was empty, head and tail both point to this node
            self.tail = node

    def _move_to_head(self, node):
        """Moves an existing node to the head of the doubly linked list."""
        self._remove(node)
        self._add_to_head(node)

    def get(self, key):
        """Retrieve item from cache. Return -1 if it doesn't exist."""
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the head (most recently used)
            self._move_to_head(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """Set the value in cache. If full, remove the least recently used item."""
        if key in self.cache:
            # If the key exists, update the value and move the node to the head
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # If the key does not exist, create a new node
            new_node = Node(key, value)
            if self.size >= self.capacity:
                # If the cache is at capacity, remove the least recently used (tail)
                del self.cache[self.tail.key]
                self._remove(self.tail)
                self.size -= 1

            # Add the new node to the head of the list and update the cache
            self._add_to_head(new_node)
            self.cache[key] = new_node
            self.size += 1

# Testing the LRU Cache

our_cache = LRU_Cache(5)

# Set values in cache
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# Get values
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

# Add more values, causing eviction
our_cache.set(5, 5)
our_cache.set(6, 6)

# 3 should have been evicted because it was the least recently used
print(our_cache.get(3))  # returns -1


# Additional Test Cases

# Test Case 1: Null-like key (key = 0)
our_cache.set(0, 0)
print(our_cache.get(0))  # returns 0

# Test Case 2: Empty or non-existent key
print(our_cache.get(10))  # returns -1 because key 10 does not exist

# Test Case 3: Large Capacity and Large Number of Elements
large_cache = LRU_Cache(1000)
for i in range(1000):
    large_cache.set(i, i*10)

print(large_cache.get(999))  # returns 9990
print(large_cache.get(1000))  # returns -1