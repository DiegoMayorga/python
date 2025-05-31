"""1. Declarar una función numero_mayor que tome dos números como parámetros y retorne el número mayor"""

# Declaración de la función
# def numero_mayor(num1, num2):
# if num1 > num2:
# return num1
# else:
# return num2

# Llamar funcion
# numero1 = int(input("Ingrese num 1: "))
# numero2 = int(input("Ingrese num 2: "))

# resultado = numero_mayor(numero1, numero2)
# print("El numero mayor es: ", resultado)

""" 2. Declara una función llamada imprimir_lista, que reciba una lista como parámetro e imprima cada elemento de la lista. """
# def imprimir_lista(lista):
# for elemento in lista:
# print(elemento)
# imprimir_lista([3, 6, "letras", True, 15])

""" 3. Llama tu función "factorial" que reciba un número entero como parámetro y retorne el factorial de ese número. """
# import math
# def factorial(numero):
# return math.factorial(numero)
# print(factorial(4))


# def factorial(num):
# if num == 1:
# return 1
# return num * factorial(num - 1)

# print(factorial(4))

""" 4. Escribe una función que revise si los parámetros recibidos son del mismo tipo de dato. Retorna True si lo son o False si no. """
# def tipo(a, b, c):
# if type(a)== type(b) and type(b) == type(c):
# return True
# else:
# return False

# print(tipo("Carro", "Lancha", 3))


""" Ejercicios diccionarios """

"""
1. Crea un diccionario vacío llamado perros."""
# perros = {}

"""
2. Agrégale al diccionario "nombre", color, "raza" y edad. La clave y el valor."""
# perros = {'"nombre"': "Max",
# '"color"': "gris",
# 'raza' : "poodle"
# }
# perros["edad"] = 4
# perros["color"] = "Blanco"
# print(perros)


"""
3. Obten el tamaño del diccionario perros.
"""
# print(len(perros))

""" 4. Crear la función es_primo que reciba un número y retorne True o False si es primo o no. """

# Un número primo solo se puede multiplicar por 1 o por sí mismo.
# 2 3 5 7 11 13 17 19

# def es_primo(num):
# if num // 1 == num and num // num == 1:
# return True

# import math

# def es_primo(numero):
# if numero < 2:
# return False
# for valor in range(2, int(math.sqrt(numero)) + 1):
# if numero % valor == 0:
# return False
# return True

""" 
estudiantes = [
  { "nombre": "Juan", "calificaciones": [80, 90, 85] },
  { "nombre": "María", "calificaciones": [70, 60, 75] },
  { "nombre": "Pedro", "calificaciones": [90, 85, 95] },
  { "nombre": "Ana", "calificaciones": [60, 75, 80] },
];

> 70 se aprueba

Crear una función que reciba un diccionario y retorne si el estudiante aprobó o no la materia. Sacar el promedio de las calificaciones para saber si pasó.

"""
# import statistics
# juan = { "nombre": "Juan", "calificaciones": [80, 90, 85] }
# maria = { "nombre": "María", "calificaciones": [70, 60, 75] }
# pedro = { "nombre": "Pedro", "calificaciones": [90, 85, 95] }
# ana = { "nombre": "Ana", "calificaciones": [60, 75, 80] }


# def aprobo(diccionario):
# notas = diccionario["calificaciones"]
# prom = statistics.mean(notas)
# if prom > 70:
# return f"aprobó con {prom}"
# else:
# return f"No aprobó con {prom}"

# print(aprobo(juan))
# print(aprobo(maria))
# print(aprobo(pedro))
# print(aprobo(ana))

""" Un Palíndromo es una palabra que se escribe igual al derecho y al revés. es_palindromo se llama la funcion y recibe un parámetro (una palabra)"""
# reconocer, sometemos, somos, ana, solos, oro, oso, ene


# def es_palindromo(palabra):
# palabra1 = list(palabra)
# if list(reversed(palabra1)) == palabra1:
# return "Es palindromo"
# else:
# return "No es palindromo"

# print(es_palindromo("somos"))

# * 1
### * 3
##### * 5
####### * 7
######### * 9
########### * 11
############# * 13

""" Crea una función arbol que no reciba parámetros y muestre la figura anterior. """
# def arbol():
# e = 6
# for p in range(1, 14, 2):
# esp = " " * e
# car = "#" * p
# print(esp + car)
# e = e - 1

# arbol()
