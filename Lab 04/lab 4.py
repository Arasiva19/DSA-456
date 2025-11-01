from typing import Any, Optional, List

# Node class
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data: Any):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after(self, target: Node, data: Any):
        if not target:
            return
        new_node = Node(data)
        new_node.next = target.next
        target.next = new_node

    def delete(self, target: Node) -> bool:
        if self.is_empty():
            return False

        if self.head == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next != target:
            current = current.next

        if current.next == target:
            current.next = target.next
            return True
        else:
            return False

    def search(self, data: Any) -> Optional[Node]:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

