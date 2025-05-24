"""
¿Cómo crear una lista?
En Python se pueden crear listas de dos maneras.
"""

# 1. Usando la función integrada list()
# lst = list([1, 2, 3, 4, 5])
# print(lst)

# lst = [1, 2, 3]
# print(lst)

# print(type(lst))

# lst = [1, "palabra", 3.14, True, [1, "palabra", (1, 2, 3)]]

# lst = [1, 2, 3, 4, 5, [1, 2, 3]]
# print(len(lst))

""" Índice en listas """

# [1, 2, 3, 4, 5]
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# lista = "hola"
# print(lista[2])
# print(lista[len(lista) - 1])

# Desempaquetando items de una lista:
# ciudad1, ciudad2, ciudad3 = ["Madrid", "Barcelona", "Valencia"]

# Cortando elementos de una lista:
# frutas = ["manzana", "pera", "naranja", "uva", "sandía"]
# print(frutas[-3:])

""" Modificando listas """
# lista = ["a", "s", "i", "o", "u"]
# lista[1] = "e"
# print(lista)

""" Revisando items de una lista """
# lista = ["a", "s", "i", "o", "u"]
# print("e" in lista)

""" Agregando items a una lista """
# lista = ["a", "b", "c"]
# lista.insert(3, "d")
# lista.append("e")

# print(lista)

""" Remover items de una lista """
# lista.pop(1)
# print(lista)

""" Limpiando una lista """
# lista.clear()
# print(lista)

""" Remover completamente una lista """
# del lista
# print(lista)