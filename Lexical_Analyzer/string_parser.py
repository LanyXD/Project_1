from collections import deque


class StringParcer:
    def __init__(self):
        self.string: str | None = None
        self.stack = deque()

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
        self._sings = "(){}\";"
        self._numbers = "0123456789"
        self._identifiers = "abcdefghijklmnopqrstuvwxyz"

    def set_string(self, string: str):
        self.string = string

    def analyze_text(self):
        if self.string is not None:
            words = self.string.split(' ')
            for word in words:
                if word in self._reserved_w:
                    self.reserved_w_c += 1
                elif word in self._operators:
                    self.operators_c += 1
                else:
                    # De momento se cuenta cada caracter, pero hay que separar los numeros de los identificadores.
                    for char in word:
                        if char in self._sings:
                            self.sings_c += 1
                        elif char in self._numbers:
                            self.numbers_c += 1
                        elif char in self._identifiers:
                            self.identifiers_c += 1
                        else:
                            raise Exception("Caracter no definido o gramaticamente incorrecto.")
        else:
            raise Exception("Cadena vacia.")


# uso de la clase
if __name__ == '__main__':
    myAnalyzer = StringParcer()
    string = "entero decimal hola <= 15jk"
    string2 = "entero decimal hola <== 15jk"

    myAnalyzer.set_string(string2)
    try:
        myAnalyzer.analyze_text()
    except:
        print("Cadena no aceptada.")
    else:
        print("Palabras reservadas: ", myAnalyzer.reserved_w_c)
        print("Operadores: ", myAnalyzer.operators_c)
        print("Signos: ", myAnalyzer.sings_c)
        print("Numeros: ", myAnalyzer.numbers_c)
        print("Identificadores: ", myAnalyzer.identifiers_c)
