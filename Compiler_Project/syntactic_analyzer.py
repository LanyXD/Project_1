from binary_tree import BinaryTree
from stack_list import StackList


class SyntacticAnalyzer:
    def __init__(self):
        self._string: str | None = None
        self.id_list: StackList | None = StackList()

        # Tokens mas expandidos
        self._type = [
            "entero",
            "decimal",
            "booleano",
            "cadena"
        ]
        self._process = [
            "si",
            "sino",
            "mientras",
            "hacer"
            ]
        self._data = [
            "verdadero",
            "falso"
        ]
        self._operators = [
            "+",
            "-",
            "*",
            "/",
            "%",
            "="
        ]

        self._comparators = [
            "==",
            "<",
            ">",
            ">=",
            "<="
        ]

        self._group = "(){}\""
        self.final = ";"
        self._numbers = "0123456789"
        self._identifiers = "abcdefghijklmnopqrstuvwxyz"

    def set_string(self, string: str):
        self._string = string

    def choose_structure(self):
        if self._string is not None:
            first = self._string.split(' ')
            if first[0] in self._type:
                self.type_structure()
            elif first[0] in self._process:
                self.process_structure()
            else:
                current = self.id_list.search(first[0])
                if current is not None:
                    self.type_structure(current)
                else:
                    raise Exception("Cadena sin identificar.")
        else:
            raise Exception("Cadena vacía.")

    def type_structure(self, current=None):
        structure = "type, Id, ;|=, data, ;"

        if current is None:
            new_tree = BinaryTree()
            self.id_list.push(new_tree)
            string = self._string.split(' ')

            new_tree.insert_right(string[1])
            string.remove(string[1])

            for word in string:
                new_tree.insert_left(word)
                new_tree.insert_right(word)

    def process_structure(self):
        print("sin implementar.")
        return self._string
