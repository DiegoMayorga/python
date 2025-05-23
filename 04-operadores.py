# ¿Qué es un booleano?

# Es un tipo de dato que representa Verdadero o Falso. En Python se escribe con la primera letra en mayúscula.

# print(True)
# print(False)

"""Operadores de asignación"""

# x = 5
# x = x + 2
# x = x - 2
# x = x * 2
# x = x / 2

# x = x % 2 # Módulo -> Residuo
# x = x // 2 # División entera
# x = x ** 2 # Potencia

# print(x)

""" Operadores aritméticos """
# + -> Suma
# - -> Resta
# etc.

""" Operadores con variables """

# num1 = 5
# num2 = 10

# print(num1 + num2)

""" Operadores de comparación """

# < menor que, > mayor que, == igual que, != diferente de, <= menor o igual que, >= mayor o igual que

# m = 2
# n = 5
# print(n < m) # False
# print(n > m) # True
# print(n == m) # False
# print(n != m) # True
# print(n <= m) # False
# print(n >= m) # True

""" Operadores lógicos """

# and, or, not

# comparar = m < n and m == n # False
# print(comparar)

# comparar_or = m < n or m == n 
# print(comparar_or)

# comparar_not = not (m < n and m == n)
# print(comparar_not)

# ejemplo_not = not (True or False)

""" 
Ejercicios:

1. Declara tu edad como una variable, luego imprímela en consola.
2. Declara tu peso como una variable, luego imprímela en consola.
3. Declara una variable que almacene un número complejo.
4. Escribe un script que le permita al usuario ingresar base y altura y con esa información calcula el área del triángulo (area = base * altura / 2).
Nota: El input() recibe un string, por lo que debes convertirlo a entero.
5. Escribe un script que le permita al usuario ingresar un lado a, lado b y lado c del triangulo. Calcula el perímetro del triángulo (perímetro = a + b + c)
6. Obten ancho y alto de un rectángulo mediante el usuario y calcula su área y perímetro (area = ancho * alto, perímetro = 2 * (ancho + alto))
7. Obten el radio de un círculo mediante el usuario y calcula el área y el perímetro (area = pi * radio ^2, perímetro = 2 * pi * radio), donde pi = 3.14
8. Halla el tamaño de la palabra "Python" y "Dragón" y genera una comparación falsa con ambos valores.
9. Halla el tamaño de "Elefante" y conviértelo a float, luego conviértelo a string.
10. Los números pares son divisibles por 2 y el residuo es cero. ¿Cómo sabes si un número es par o impar?
11. Confirma si la división entera entre 7 y 3 es igual al valor 2.7 convertido a entero.
12. Confirma si el tipo de "10" es igual al tipo de 10. Recuerda usar type()
13. Confirma si int('9.8') es igual a 10.
"""
# 5 + 5j

# edad = 17
# print(edad) # 17

# peso = "58,6"
# print(peso) # 58,6

# comp = 2 + 2j
# print(comp) # (2 + 2j)



# altura = int(input("Ingrese la altura del triangulo: "))
#  base = int(input("Ingrese la base de su triangulo: "))
# area_trian = (base * altura) / 2
# print("El area del triangulo es: ", int(area_trian))

lado1 = int(input("Ingrese el valor del primer lado del triangulo"))
lado2 = int(input("Ingrese el valor del segundo lado del triangulo"))
lado3 = int(("Ingrese el valor del tercer lado del triangulo"))

