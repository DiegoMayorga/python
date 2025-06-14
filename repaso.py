"""
Ejercicios:

# Listas:

1. Crea una lista vacía, una tupla vacía, un conjunto vacío y un diccionario vacío e imprímelas.
2. Obten el primer item de tu lista.
3. Crea una lista de 6 números e imprime el primero, el tercero y el último número de la lista.
4. Crea una lista y modifícala con append.
5. Modifica la lista anterior insertando un elemento en el índice 2.
6. Verificar que uno de los elementos esté en la lista.
"""

# 1.
# lista = list()
# tupla = tuple()
# conjunto = set()
# diccionario = dict()
# print(lista, tupla, conjunto, diccionario)

# 2.
# nums = [1, 2, 3, 4, 5]
# print(nums[0])

# 3.
# nums = [1, 2, 3, 4, 5, 6]
# print(nums[0], nums[2], nums[5])

# 4.
# nums = [1, 2, 3, 4, 5, 6]
# nums.append("Hola :)")
# print(nums)
# nums = [1, 2, 3, 4, 5, 6]
# letters = ["a", "b", "c"]
# nums.extend(letters)
# print(nums)

# nombre_apellido = ["Maria", "Luis", "Perez", "Carlos", "Rincon", "Ana", "Ruiz"]
# nombre_apellido.insert(1, "Jaramillo")
# nombre_apellido.extend(["Juan", "Diaz"])
# print(nombre_apellido)

"""
# Tuplas:

1. Crea 3 tuplas, una de 2 frutas, otra de 2 bebidas y otra de 2 dulces. Junta las 3 tuplas y guárdalas en una variable llamada comidas.
2. Limpiar la tupla de comidas. Imprímela.
3. Crea una tupla y modifica sus dos últimos valores.
4. Dada la siguiente tupla:

paises_de_lationamerica = ("Colombia", "Perú", "Brasil")

* Verifica si "Portugal" es un país de Latinoamérica.
* Verifica si "Brasil" es un país de Latinoamérica.
"""
# 1.
# frutas = ("Mango", "Fresa")
# bebidas = ("Sprite", "Fanta")
# dulces = ("Splot", "Trululu")
# comidas = list(frutas) + list(bebidas) + list(dulces)
# comidas1 = tuple(comidas)
# print(comidas1)

# 2.
# lista1 = list(comidas1)
# lista1.clear()
# print(tuple(lista1))

# 3.
# frutas = ("Mango", "Fresa", "Lulo")
# frutas1 = list(frutas)
# frutas1.pop(1)
# frutas1.remove("Lulo")
# del frutas1[0]
# print(frutas1)

# 4.
# paises_de_latam = ("Colombia", "Perú", "Brasil")
# print("Brasil" in paises_de_latam)
# print("portugal" in paises_de_latam)

"""
# Conjuntos:

Ejercicios Nivel 1:

1. Dado este conjunto:

empresas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

a. Agrega "Temu" al conjunto "empresas"
b. Elimina una de las empresas del conjunto
c. Imprime todo.

"""

# empresas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# empresas.add("Temu")
# empresas.remove("Facebook")
# print(empresas)


"""
Ejercicios Nivel 2:

2. Dado este conjunto:

a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

a. Junta a y b.
b. Encuentra la intersección entre a y b
c. ¿Es a un subconjunto de b?
d. Imprime todo
"""
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# a.update(b)
# a.intersection(b)
# print(a)
# print(a.issubset(b))

"""
Ejercicio Nivel 3:

3. Dada esta lista:

age = [22, 19, 24, 25, 26, 24, 25, 24]

a. Convierte las edades a un conjunto y compara el tamaño de la lista y del conjunto. ¿Cuál es más grande?
"""
# age = [22, 19, 24, 25, 26, 24, 25, 24] # 8
# age1 = set(age) # 5
# print(len(age) < len(age1))
# print(age)
# print(age1)

"""
Diccionarios:

1. Crea un diccionario vacío llamado animales.
2. Agrégale al diccionario nombre, color, tamaño y edad. La clave y el valor.
3. Obten el tamaño del diccionario animales.
4. Obten las claves del diccionario.
5. Obten los valores del diccionario.
6. Elimina uno de los items del diccionario.
7. No olvides imprimir todo.

"""

# animales = {}
# animales["nombre"] = "Caballo"
# animales["color"] = "Café"
# animales["tamaño"] = "Grande"
# animales["edad"] = 13
# print(animales)
# print(len(animales))
# print(animales.keys())
# print(animales.values())
# animales.pop("tamaño")
# print(animales)

""" Anagrama """
# Crear una función llamada is_anagram que reciba dos parámetros (dos palabras) y retorne True o False según si es anagrama o no.
# def is_anagram(pal1, pal2):
# if len(pal1) != len(pal2):
# return False
# org1 = sorted(pal1)
# org2 = sorted(pal2)
# if org1 == org2:
# return True
# else:
# return False

# print(is_anagram("roma","tres"))


# texto = "python"
# ordenado = sorted(texto)

# sorted(lista, reverse=True)

""" Crear una función llamada distancia_entre que reciba una lista como parámetro y retorne la distancia entre el primer y último elemento de la lista. """
# La lista debe ser ordenada en la función.
# [1, 5, 7, -5, -3, -4]
# ["-5", "-8", 8, 4, 2]
# def distancia_entre(lista):
# new = []
# for i in lista:
# if type(i) != type(1):
# new.append(int(i))
# else:
# new.append(i)
# ord = sorted(new)
# dist = ord[-1] - ord[0]
# return dist

# b = ["-5", "-50", 8, -10, 2]
# print(distancia_entre(b))

""" Split, join """

# frase = "Hola Python, este es un ejemplo"
# frase2 = "Hola%Mundo%Python"
# print(frase.split(","))
# dividir_palabra = frase2.split("%")
# print(",".join(dividir_palabra))

# lst = [1, 5, 6, 2, 4]
# print(sorted(lst))

# Tomar un string con números y convertirla a una fecha con esta estructura: DD/MM/YYYY
# fecha1 = "2018*05*12" 05 de diciembre de 2018
# fecha2 = "hola+mundo/15.02.2018" 15 de febrero de 2018
# fecha3 = "2018.02.15-mundo*hola" 15 de febrero de 2018
# fecha1 = "2018*05*12"
# data = fecha1.split("*")
# data1 = []
# data1.append(data[1])
# data1.append(data[2])
# data1.append(data[0])
# print("/".join(data1))
# fecha2 = "hola+mundo/15.02.2018"
# data = fecha2.split("/")
# data1 = []
# data1.append(data[1])
# fecha = "".join(data1)
# data1 = fecha.split(".")
# print("/".join(data1))

# fecha3 = "2018.02.15-mundo*hola"
# data = fecha3.split("-")
# data1 = []
# data1.append(data[0])
# fecha = "".join(data1)
# fecha1 = fecha.split(".")
# fecha1.reverse()
# print("/".join(fecha1))

