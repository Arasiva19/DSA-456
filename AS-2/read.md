Answer for part 3

insert(self, data)
This function puts a new value into the list in the right order so the list stays sorted.
It starts from the beginning and moves through the list until it finds the correct place to add the new node.
If the list is long, it might have to check every node one by one.
So, it takes more time when the list is big.
Time complexity: O(n)

remove(self, data)
This function looks for a node that has the value we want to remove.
It goes through each node until it finds it.
Once found, it connects the previous and next nodes together so the list stays linked.
If the value isn’t there, it will reach the end of the list.
Time complexity: O(n)

is_present(self, data)
This one just checks if a certain value exists in the list.
It starts from the first node and compares each one.
If it finds the data, it stops early; if not, it checks all of them.
Time complexity: O(n)

__len__(self)
This function gives back the total number of items in the list.
Since we already keep track of the size whenever we add or remove nodes, this function just returns that number right away.
It doesn’t have to go through the list.
Time complexity: O(1)