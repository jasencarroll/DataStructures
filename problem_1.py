from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity  # maximum size of the cache
        self.cache = OrderedDict()  # OrderedDict to store the cache elements

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            # If key is found, move it to the end (mark as most recently used)
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if key in self.cache:
            # If key is already present, just update the value and mark it as most recently used
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # If the cache has reached capacity, pop the first item (least recently used)
            self.cache.popitem(last=False)

        # Insert the new key-value pair into the cache
        self.cache[key] = value

# Testing the cache

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

# Add your own test cases: include at least three test cases
## Test Case 1: Testing with null-like key
our_cache.set(0, 0)  # setting key 0
print(our_cache.get(0))  # returns 0, key 0 exists in cache

## Test Case 2: Testing with empty or non-existent key
print(our_cache.get(10))  # returns -1, key 10 doesn't exist

## Test Case 3: Testing with a large capacity and a large number of elements
large_cache = LRU_Cache(1000)
for i in range(1000):
    large_cache.set(i, i*10)  # set values

print(large_cache.get(999))  # returns 9990, because it should be present
print(large_cache.get(1000))  # returns -1, because it doesn't exist