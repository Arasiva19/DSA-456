1. __len__(self) – O(C)
This method determines how many records are currently stored by scanning the entire internal list. Because it checks every slot in the table (even the empty ones), the running time depends on the table’s capacity rather than the number of actual records. For that reason, the complexity is O(C).

2. search(self, key) – O(C + n) → effectively O(n)
The search operation begins by calling len(self), which already takes O(C) time since it scans the whole table. After that, the function walks through the stored records in a simple linear manner until the key is found or all items are checked. In the worst case, it inspects every record. Combining both steps gives O(C + n), which simplifies to O(n) because C grows with the table.

3. insert(self, key, value) – O(n²)
The insert function is the slowest of them all. It first calls search(key) (a linear operation). If the table is full, it performs a resize and copies all existing elements, which is O(C). After inserting the new record at the end, the table runs a bubble sort to restore sorted order. Since bubble sort takes O(n²) time, this dominates the overall cost, making insertion O(n²).

4. modify(self, key, value) – O(n)
To update a record’s value, the function goes through the list one item at a time until it finds the key. This is simply a linear search across the stored elements, giving it O(n) complexity. Although it calls len(self) repeatedly in the loop condition, the overall behaviour stays linear.
5. remove(self, key) – O(n)
Removing a record also requires a linear search to locate the correct key. Once it finds the target, the function shifts all the following elements one position left. In the worst case—removing the first element—this shift covers almost the entire list. Both the search and the shift are linear operations, so removal runs in O(n) time.
6. capacity(self) – O(1)
This method simply returns the table’s capacity. It does not scan or compute anything, so it operates in constant time, O(1).

| Function   | Complexity | Explanation                                     |
| ---------- | ---------- | ----------------------------------------------- |
| `insert`   | **O(n²)**  | Uses bubble sort after adding each new record.  |
| `modify`   | **O(n)**   | Linearly scans until the key is found.          |
| `remove`   | **O(n)**   | Searches for the key and shifts later items.    |
| `search`   | **O(n)**   | Walks through stored records until key matches. |
| `capacity` | **O(1)**   | Returns the capacity directly.                  |
| `__len__`  | **O(C)**   | Counts entries by scanning the entire list.     |

