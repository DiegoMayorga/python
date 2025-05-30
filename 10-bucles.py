"""Bucles"""

# Para manejar tareas repetitivas en programación, se utilizan los bucles. Python ofrece el bucle while y el for.

""" Bucle while """

# Usamos la palabra reservada "while" para hacer un bucle while. Es usado para ejecutar un bloque de declaraciones repetidas hasta que una condición
# se satisfaga. Cuando la condición se vuelve falsa, continúa el script con las siguientes líneas de código.

# x = 0

# while x < 10:
# print(x)
# x = x + 1
# if x == 5:
# continue
# print("Hola")
# else:
# print("El valor no es menor que 10")

# print("Terminó de repetirse el bucle while.")

# Con la palabra reservada break nos salimos del bucle

""" Bucle for """

# La palabra reservada for es usada para hacer un bucle for, similar a otros lenguajes de programación, pero con algunas diferencias de sintaxis.
# Con este bucle se puede iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o string)

# lista = [1, 2, 3, 4]
# conjunto = {"a", "b", "c", "d"}
# tupla = (1, 2, 3, 4)
# palabra = "Hola Python"

# for elemento in palabra:
# print(elemento)

""" 
Ejercicios:

Nivel 1:

1. Recorrer del 0 al 10 usando el bucle for.

range(8) 0 al 7
range(2,9) 2 al 8
range(0, 8, 2) 0 2 4 6 

"""
# c = range(11)
# for i in c:
# print(i)


"""
2. Iterar del 10 al 0 usando el bucle while.

"""
# i = 10
# while i > -1:
    # print(i)
    # i = i - 1



"""
3. Escribe un bucle que haga 7 llamadas a print(), para obtener el siguiente dibujo:

#
##
###
####
#####
######
#######
"""
# e = 1
# while e < 8:
# print("#" * e)
# e = e + 1  

""" print(
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100     
) """

"""
4. Imprime el siguiente patrón:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

5. Itera con el bucle for la lista ["Cálculo", "Programación", "Inglés"]

Nivel 2:

6. Usa el bucle for para iterar de 0 a 100 e imprime la suma de todos esos números. 0 + 1 + 2 + ... + 100
7. Usa el bucle for para iterar de 0 a 100 e imprime la suma de todos los números pares. 0 + 2 + 4 + ... + 100

"""
