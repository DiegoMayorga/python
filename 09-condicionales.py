"""Condicionales"""

# Por defecto, las declaraciones en los scripts de Python se ejecutan secuencialmente. De arriba a abajo.
# Si el proceso lógico lo requiere, el flujo secuencial puede ser alterado en dos formas:

# Ejecución condicional: Un bloque de una o más declaraciones será ejecutado si una expresión es verdadera.
# Ejecución repetitiva: Un bloque de uno o más declaraciones será ejecutada repetidamente mientras una determinada expresión sea verdadera.

""" Condicional If (Si) """

# if
# elif
# else

""" color_fav = input("¿Cuál es tu color favorito? ")
if color_fav == "rojo":
    print("Tu color favorito es rojo")
elif color_fav == "verde":
    print("Tu color favorito es verde")
else:
    print("No se cuál es ese color") """

# a = 5
# print("El numero es positivo") if a > 0 else print("El numero es negativo")

x = int(input("Ingresa un numero: "))
if x % 2 == 0 and x >= 0:
    print("Este numero es par y positivo.")
elif x % 2 == 0 and x < 0:
    print("Este numero es par y negativo.")
elif x % 2 != 0 and x > 0:
    print("Este numero es impar y positivo.")
else:
    print("Este numero es impar y negativo.")