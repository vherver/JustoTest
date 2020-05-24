"""
Problema 1: Dado el Input (una lista de id’s de ordenes representados por números enteros),
crear una función que regrese el Output
especificado de la manera más eficiente posible. Justifica tu respuesta.
Lenguaje Recomendado: Python
Input [123, 1, 321, 45, 54, 23, 12, 21, 231]
Output [
[123,321,231],
[1],
[45, 54],
[23],
[12,21]
]
"""
from itertools import permutations


def new_order(lista):
    new_list = []

    while len(lista) > 0:
        temp_list = []
        number_str = list(str(lista[0]))
        permutaciones = permutations(number_str)
        res = list(map("".join, permutaciones))
        for permutation in res:
            try:
                index = lista.index(int(permutation))
                temp_list.append(lista.pop(index))
            except ValueError:
                pass
        new_list.append(temp_list)

    return new_list


if __name__ == "__main__":

    initial_list = [123, 1, 321, 45, 54, 23, 12, 21, 231]
    print(new_order(initial_list))
