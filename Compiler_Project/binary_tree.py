from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        return str(self.data)


class BinaryTree(Generic[T]):
    def __init__(self):
        self.root: Node | None = None

    def insert_left(self, data: T, ref: T | None = None):
        new_node = Node(data)
        if ref is None:
            self.root = new_node
        else:
            node_ref = self.search(ref, self.root)
            if node_ref is not None:
                node_ref.left = new_node

    def insert_right(self, data: T, ref: T | None = None):
        new_node = Node(data)
        if ref is None:
            self.root = new_node
        else:
            node_ref = self.search(ref, self.root)
            if node_ref is not None:
                node_ref.right = new_node

    def __preorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{subtree.data} - {self.__preorder(subtree.left)} - {self.__preorder(subtree.right)}"

        return result

    def __inorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{self.__inorder(subtree.left)} - {subtree.data} - {self.__inorder(subtree.right)}"

        return result

    def __postorder(self, subtree: Node | None) -> str:
        result = 'None'

        if subtree is not None:
            result = f"{self.__postorder(subtree.left)} - {self.__postorder(subtree.right)} - {subtree.data}"

        return result

    def preorder(self) -> str:
        return self.__preorder(self.root)

    def inorder(self) -> str:
        return self.__inorder(self.root)

    def postorder(self) -> str:
        return self.__postorder(self.root)

    def __get_path(self, ref: T, subtree: Node | None) -> str:
        if subtree is None:
            return ''

        elif subtree.data == ref:
            return 'Node'

        if subtree.left is not None:
            left = self.__get_path(ref, subtree.left)
            if left is not None:
                return f'Left - {left}'

        if subtree.right is not None:
            right = self.__get_path(ref, subtree.right)
            if right is not None:
                return f'Right - {right}'

    def get_path(self, ref):
        return self.__get_path(ref, self.root)

    def search(self, ref: T, subtree: Node | None = None) -> Node | None:

        if subtree is None:
            return None
        elif subtree.data == ref:
            return subtree

        if subtree.left is not None:
            left = self.search(ref, subtree.left)
            if left is not None:
                return left

        if subtree.right is not None:
            right = self.search(ref, subtree.right)
            if right is not None:
                return right

    def __str__(self):
        return str(self.root.data)
