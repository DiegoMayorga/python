"""Funciones"""

# Una función es un bloque reutilizable de código o declaración de programación diseñada para realizar una tarea específica.
# Para definir o declarar una función, Python usa la palabra reservada def. Con la siguiente sintaxis se puede definir una función
# (El bloque de código de la función es ejecutado solo si la función es llamada o invocada)

# Declarar la función
# def mi_funcion():
# return 1 + 1

# Llamar la función
# print(mi_funcion())

# () no tiene argumentos
# (hola, mundo) 2 argumentos

# def otra_funcion():
    # return 5

# print(otra_funcion())

# Declarar la función
# def nombre_completo(nombre, apellido):
    # espacio = " "
    # return nombre + espacio + apellido

# Llamar la función
# print(nombre_completo("Pedro", "Perez"))
# print(nombre_completo("Lucia", "Gomez"))
# print(nombre_completo("Maria", "Reyes"))

# def suma(num1 = 5, num2 = 10):
     # return num1 + num2
 
# print(suma(250, 3))

"""
Ejercicio: El area de un círculo se calcula con la fórmula A = π * r^2, donde A es el área y r es el radio. Escribe una función
que calcule el área de un círculo recibiendo el radio como parámetro y utilizando π como 3.14.
"""

""" Definiendo la funcion """
def area_cir(radio):
    pi = 3.14
    area = (radio * radio) * pi
    return "El area del circulo es: ", area

""" Llamar la funcion """

radio = float(input("Ingrese el radio de su círculo: "))
print(area_cir(radio))