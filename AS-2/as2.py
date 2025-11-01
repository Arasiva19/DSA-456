# Doubly Linked List with Sentinel Node (Sorted)

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        # Sentinel node simplifies insert/remove edge cases
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0

    # Show the list contents
    def show(self):
        current = self.sentinel.next
        elems = []
        while current != self.sentinel:
            elems.append(current.data)
            current = current.next
        print("Lcist:", elems)
        return elems

    # Get first element
    def get_front(self):
        if self.size == 0:
            return None
        return self.sentinel.next.data

    # Get last element
    def get_back(self):
        if self.size == 0:
            return None
        return self.sentinel.prev.data

    # Insert at the front (ignores sorting)
    def insert_front(self, data):
        node = Node(data)
        first = self.sentinel.next
        node.next = first
        node.prev = self.sentinel
        first.prev = node
        self.sentinel.next = node
        self.size += 1

    # Insert at the back (ignores sorting)
    def insert_back(self, data):
        node = Node(data)
        last = self.sentinel.prev
        node.prev = last
        node.next = self.sentinel
        last.next = node
        self.sentinel.prev = node
        self.size += 1

    # Insert keeping the list sorted (ascending)
    def insert(self, data):
        node = Node(data)
        current = self.sentinel.next
        while current != self.sentinel and current.data < data:
            current = current.next

        # insert before current
        node.next = current
        node.prev = current.prev
        current.prev.next = node
        current.prev = node
        self.size += 1

    # Remove a node with given data
    def remove(self, data):
        current = self.sentinel.next
        while current != self.sentinel:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    # Check if data is present
    def is_present(self, data):
        current = self.sentinel.next
        while current != self.sentinel:
            if current.data == data:
                return True
            current = current.next
        return False

    # Return number of elements
    def __len__(self):
        return self.size


# ------------------ Testing ------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert data in random order
    for x in [5, 2, 8, 1, 3]:
        ll.insert(x)

    ll.show()
    print("Front:", ll.get_front())
    print("Back:", ll.get_back())
    print("Present(3):", ll.is_present(3))
    print("Remove(2):", ll.remove(2))
    ll.show()
    print("Length:", len(ll))
