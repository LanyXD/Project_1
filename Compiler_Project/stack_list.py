from typing import TypeVar, Generic


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)


class StackList(Generic[T]):
    def __init__(self, maximus=-1):
        self.head: None | Node = None
        self.size: int = 0
        self.max: int = maximus

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data: T):
        if self.max == -1 or self.size < self.max:
            new_node = Node(data)
            self.size += 1

            if not self.is_empty():
                new_node.next = self.head

            self.head = new_node

        else:
            raise Exception("Overflow error")

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("Underflow error")
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1

            return current

    def clear(self):
        while self.head is not None:
            self.pop()

        self.size = 0

    def search(self, data):
        current = self.head

        while current is not None:
            print(data)
            print(current.data)
            print(current.data.data)
            if current.data == data:
                return current

            current = current.next

        return None

    def transversal(self) -> str:
        result = ''
        current = self.head

        while current is not None:
            result += f"{current} "

            if current.next is not None:
                result += "-> "

            current = current.next

        return result
