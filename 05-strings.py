""" El texto es un tipo de dato String, también se le llama cadena de texto """

# 1. Crear un string

# letter = "p"                     # Un string puede ser un simple caracter o un texto largo
# print(letter)                    # p
# print(len(letter))               # 1
# saludo = 'Hola, Mundo'           # Un string se puede escribir entre comillas simples o dobles. 'Hola, Mundo' tambien es váludo.
# print(saludo)                    # Hola, Mundo
# print(len(saludo))               # 11
# frase = "Esto es un texto largo"
# print(frase)

# String de múltiples líneas

# string_multilinea = """
# Esto es un texto largo
# con múltiples líneas
# """

# print(string_multilinea)

# 2. Concatenación de strings

# primer_nombre = "Diego"
# apellido = "Mayorga"
# espacio = " "
# print(primer_nombre + espacio + apellido)

# 3. Secuencias de escape en strings

# En Python y otros lenguajes de programación, \ seguido de un caracter es una secuencia de escape. Estas son las más comunes:

# \n: salto de línea
# \t: tabulación
# \\: caracter de barra invertida
# \': comilla simple
# \": comilla doble

# print("Esto es un texto largo\ncon un salto de línea")
# print("Esto es un texto largo\tcon un tabulación")
# print("Esto es un texto largo\\con un caracter de barra invertida") # Se usa más que todo para imprimir rutas, como C:\\Users\\Usuario\\Documents\\
# print("C:\\Users\\Usuario\\Documents\\")
# print("Hola \"mundo\"")

# 4. Formateo de strings

# 4.1 Forma antigua de formatear strings con el operador %
# %s : cadena
# %d : entero
# %f : número decimal
# %.<n>f : número decimal con n digitos después del punto decimal
# fn = 'Diego'
# ln = 'Mayorga'
# language = 'Python'

# fn = 'Diego'
# ln = 'Mayorga'
# language = 'Python'

# print("I am %s %s. I teach %s" %(fn, ln, language))

# 4.2 Otra forma de formatear strings (str.format) (también antigua)

# nombre = "Diego"
# apellido = "Mayorga"
# edad = 24

# print("Mi nombre es {} {} y tengo {} años.".format(nombre, apellido, edad))

# 4.3 Forma más actual de formatear strings (f-strings o interpolación de strings)

# a = 5
# b = 3

# print(f"{a} + {b} = {a + b}") # 5 + 3 = 8

# palabra1 = "Mi"
# palabra2 = "nombre"

# print(f"1: {palabra1} y 2 es: {palabra2} {palabra1 + palabra2}") # 1: Mi y 2 es: nombre Minombre
# print("Palabra 1: ", palabra1, "Palabra 2: ", palabra2)

# 5. Strings de Python como secuencia de caracteres

# lenguaje = "Python"
# a, b, c, d, e, f = lenguaje
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# 6. Accediendo a caracteres en strings por índice

# En programación, se empieza a contar desde el 0. Por tanto, la primera letra de un string tiene índice 0, la segunda 1 y así sucesivamente.

# palabra ['P', 'y', 't', 'h', 'o', 'n']
# indice    0    1    2    3    4    5
# indice   -6   -5   -4    -3   -2   -1

# lenguaje = "Python"
# x = lenguaje[5]
# print(x)

# palabra = input("Ingrese una palabra: ")
# ultima_letra = palabra[-1]
# print(ultima_letra)

""" Hasta aqui el dia 1 """
