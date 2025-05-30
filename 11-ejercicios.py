"""
Ejercicios:


# Listas:

1. Crea una lista vacía, una tupla vacía, un conjunto vacío y un diccionario vacío e imprímelas.
2. Crea una lista con más de 5 ítems y halla su tamaño.
3. Obten el primer item de tu lista.
4. Crea una lista de 6 números e imprime el primero, el tercero y el último número de la lista.
5. Agrega un número a la lista e imprímela.
6. Crea una lista con 3 apellidos. Luego, ordena la lista con el método sort()
7. Verifica si un apellido está en tu lista.

Agregar items a una lista: append()
"""
# lista1 = [20, 35, "fresa", True, 3]
# print(len(lista1))
# print(lista1[0])
# lista1.append("mango")
# print(lista1)



"""

# Tuplas:

1. Crea 3 tuplas, una de frutas, otra de bebidas y otra de dulces. Junta las 3 tuplas y guárdalas en una variable llamada comidas. Imprímela.
2. Elimina completamente la tupla de comidas. Imprímela.
3. Dada la siguiente tupla:

paises_de_lationamerica = ("Colombia", "Perú", "Brasil")

* Verifica si "Portugal" es un país de Latinoamérica.
* Verifica si "Brasil" es un país de Latinoamérica.

"""
# tupla1 = ("Mora", "Banano")
# tupla2 = ("Fanta", "Sprite")
# tupla3 = ("Gomitas", "Chocolatina")
# comidas = tupla1 + tupla2 + tupla3
# print(comidas)
# del comidas
# print(comidas)
# print("fresa" in comidas)

"""
# Conjuntos:

Ejercicios Nivel 1:

1. Dado este conjunto:

empresas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

a. Encuentra el tamaño del conjunto "empresas"
b. Agrega "Temu" al conjunto "empresas"
c. Elimina una de las empresas del conjunto
d. Imprime todo.
"""

# empresas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# empresas.add("Temu")
# print(empresas)
# empresas.remove('Google')
# print(empresas)
# empresas.discard('Temu')


"""
Ejercicios Nivel 2:

2. Dado este conjunto:

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

a. Junta A y B.
b. Encuentra la intersección entre A y B.
c. ¿Es A un subconjunto de B?
d. Imprime todo
"""
# a = {2, 4, 6}
# b = {0, 2, 4, 6, 8}
# print(a.issubset(b))


"""
Ejercicio Nivel 3:

3. Dada esta lista:

age = [22, 19, 24, 25, 26, 24, 25, 24]

son_iguales = len(age) == len(age2)
"""
age = [22, 19, 24, 25, 26, 24, 25, 24]
conjunto = set(age) # {22, ...}
print(len(age) == len(conjunto))
print(age)
print(conjunto)

otro_conjunto = {22, 19, 24, 25, 26, 24, 25, 24}
print(otro_conjunto)

# Los elementos de los conjuntos se agrupan si son iguales

"""
a. Convierte las edades a un conjunto y compara el tamaño de la lista y del conjunto. ¿Cuál es más grande?

Diccionarios:

1. Crea un diccionario vacío llamado perros.
2. Agrégale al diccionario nombre, color, raza y edad. La clave y el valor.
3. Obten el tamaño del diccionario perros.
4. Obten las claves del diccionario.
5. Obten los valores del diccionario.
6. Elimina uno de los items del diccionario.
7. No olvides imprimir todo.

"""