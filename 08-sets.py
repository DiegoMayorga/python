""" Sets (en español, conjuntos) """
# Son una colección de items. Es una colección de distintos elementos sin orden ni índice. En Python los Sets son usados para almacenar items únicos y es posible encontrar
# la unión, intersección, diferencia, diferencia simétrica, subconjunto, super conjunto y conjunto desarticulado.

# s = set()
# s = {}

conjunto2 = set({"casa", "perro", "gato", "ratón", "elefante"})
conjunto = {"casa", "perro", "gato", "ratón", "elefante"}

""" Accediendo a los items de un set """
# Para acceder a los items de un set, se pueden usar bucles, eso lo veremos en la sección de bucles.

""" Comprobar si un item está en un set """
# s = {"casa", "perro", "gato", "ratón", "elefante"}
# print("casa" in s)

""" Agregar items a un set """
# items = {"casa", "perro", "gato", "ratón", "elefante"}
# print(items)

# items.add(1)
# print(items)

# items.update({1, 2, 3})
# print(items)

""" Eliminar items de un set """
# discard, remove
# items = {"casa", "perro", "gato", "ratón", "elefante"}
# items.remove("casa")
# items.discard("casa")
# items.discard("perro")
# print("perro" in items)

""" Intersección de sets """

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}

# print(set1.intersection(set2))

""" Sub conjunto super conjunto """

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}

print(conjunto2.issuperset(conjunto1))