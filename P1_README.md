## LRU

### Key Concepts:

1. **Cache with a fixed capacity**: 
   - The LRU cache has a set capacity, meaning it can only store a fixed number of items. Once this capacity is reached, if a new item is added, the **least recently used** item (the item that hasn’t been accessed for the longest time) is **removed** to make room for the new item.

2. **Least Recently Used (LRU) Strategy**:
   - The LRU cache evicts the **least recently used** item when it’s full. So, every time you access or add an item to the cache, it becomes the **most recently used** item, and items that haven't been accessed in a while move towards the "least recently used" end of the list.

### How a Doubly Linked List Fits In:

In the LRU cache, a **doubly linked list** helps efficiently manage this **most-recently-used vs. least-recently-used** ordering.

- **Head**: The head of the doubly linked list is the **most recently used** item.
- **Tail**: The tail of the doubly linked list is the **least recently used** item.

### Operations in the LRU Cache:

1. **Accessing a Cached Item (`get`)**:
   - When you access an item, you need to move it to the **front (head)** of the doubly linked list because it’s now the **most recently used**.
   - If the item isn't found in the cache (i.e., it doesn't exist), return `-1`.

2. **Adding a New Item (`set`)**:
   - If the cache is **not full**, add the new item at the **head** of the doubly linked list, because it's now the **most recently used**.
   - If the cache **is full**, remove the item at the **tail** of the doubly linked list (since it's the least recently used) and then add the new item to the head.

### Example of LRU Cache in Action:

Let’s walk through an example to solidify the concept.

#### Scenario:
- **Capacity**: 3
- Cache starts empty.

#### Step-by-Step:

1. **Set 1:1** → Cache: `[1]`
   - The cache is empty, so we add `1` to the head of the list.

2. **Set 2:2** → Cache: `[2, 1]`
   - Add `2` to the head, `1` becomes less recently used.

3. **Set 3:3** → Cache: `[3, 2, 1]`
   - Add `3` to the head. Now `1` is the least recently used.

4. **Get 1** → Cache: `[1, 3, 2]`
   - Accessing `1` means we move it to the head, marking it as the most recently used. Now `2` is the least recently used.

5. **Set 4:4** → Cache: `[4, 1, 3]`
   - Capacity is full, so we remove `2` (the least recently used item at the tail) and add `4` to the head.

6. **Get 3** → Cache: `[3, 4, 1]`
   - Accessing `3` moves it to the head. Now `1` is the least recently used.

### Efficiency of Using a Doubly Linked List:

- **Efficient updates**: When you access an item, the doubly linked list lets you quickly move the accessed item to the head (most recently used) and remove the least recently used item from the tail in **constant time** O(1).
- **Dictionary (hash map) integration**: To efficiently retrieve an item in constant time O(1), we combine the doubly linked list with a **hash map (dictionary)**. The dictionary maps keys to the corresponding nodes in the list, allowing for fast lookups.

### Summary:

- The **LRU Cache** is a combination of a **doubly linked list** and a **hash map**.
- The **doubly linked list** keeps track of the order of usage of the items, with the head representing the most recently used item and the tail representing the least recently used.
- The **hash map** allows for fast access to cache items by key, and the doubly linked list allows for efficient reordering when items are accessed or removed.
  
By combining these two data structures, the LRU cache ensures that both retrieval and insertion operations are efficient, even as items are accessed and evicted based on their usage. 