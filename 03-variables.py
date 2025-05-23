"""Nombres válidos para variables en Python"""

# firstname
# lastname
# age
# country
# city
# first_name
# last_name
# capital_city
# _if # si se quieren usar palabras reservadas como variables, se pueden usar con guion bajo.
# year_2021
# year2021
# current_year_2021
# birth_year
# num1
# num2

""" Nombres no válidos o no recomendados para variables en Python """

# first-name
# first@name
# first$name
# num-1
# 1num

nombre = "Juan"
apellido = "Pérez"
edad = 30
habilidades = ["Python", "Java", "JavaScript"]
es_casado = True

print(nombre)
print(habilidades)

""" Debilmente Tipado """

nombre = "Maria"
nombre = "Luis"
nombre = 10

print(nombre)

nombre, apellido, edad = "Carlos", "Perez", 30
print(edad)