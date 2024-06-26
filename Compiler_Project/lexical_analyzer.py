from stack_list import StackList


class LexicalAnalyzer:
    def __init__(self):
        self.string: str | None = None
        self.stack = StackList()

        # Contadores de los tokens
        self.reserved_w_c: int = 0  # Contador palabras reservadas
        self.operators_c: int = 0  # Contador operadores
        self.sings_c: int = 0  # Contador signos
        self.numbers_c: int = 0  # Contador numeros
        self.identifiers_c: int = 0  # Contador identificadores

        # Tokens
        self._reserved_w = [
            "entero",
            "decimal",
            "booleano",
            "cadena",
            "si",
            "sino",
            "mientras",
            "hacer",
            "verdadero",
            "falso"
        ]
        self._operators = [
            "+",
            "-",
            "*",
            "/",
            "%",
            "=",
            "==",
            "<",
            ">",
            ">=",
            "<="
        ]
        self._sings = "(){};\""
        self._numbers = "0123456789"
        self._identifiers = "abcdefghijklmnopqrstuvwxyz"

    def set_string(self, text: str):
        self.string = text

    def analyze_text(self):
        if self.string is not None:
            text = self._analyze_sings()        # analiza el texto y los signos que contiene, ademas de eliminarlos.
            words = text.split(' ')
            for word in words:
                word = word.replace("\r", "")
                self._analyze_word(word)        # analiza el resto del texto palabras reservadas, operaciones, id y num.
        else:
            print("cadena vacia.")
            raise Exception("Cadena vacia.")    # Error cadena vacia.

    # Analiza y retorna la cadena sin signos
    def _analyze_sings(self) -> str:
        text_without_s = ""
        self.stack.clear()

        for char in self.string:
            if char not in self._sings:
                text_without_s += char
            else:
                self.sings_c += 1

                if char == "(":
                    self.stack.push("(")
                elif char == "{":
                    self.stack.push("{")
                elif char == ")":
                    if self.stack.head.data == "(":
                        self.stack.pop()
                    else:
                        raise Exception("Error de parentesis.")
                elif char == "}":
                    if self.stack.head.data == "{":
                        self.stack.pop()
                    else:
                        raise Exception("Error de parentesis.")

        if self.stack.size >= 1:
            raise Exception("Error de parentesis.")

        return text_without_s

    # Analiza las palabras reservadas, id, num, y otros.
    def _analyze_word(self, word):
        if word in self._reserved_w:
            self.reserved_w_c += 1
        elif word in self._operators:
            self.operators_c += 1
        else:
            flag = True
            number = ""
            for char in word:
                if char in self._numbers:
                    number += char
                elif char in self._identifiers:
                    flag = False
                else:
                    raise Exception("Cadena no aceptada.")

            if flag:
                self.numbers_c += 1
            else:
                self.identifiers_c += 1

    def results(self):
        return [self.reserved_w_c, self.operators_c, self.sings_c, self.numbers_c, self.identifiers_c]
