"""Bucles"""

# Para manejar tareas repetitivas en programación, se utilizan los bucles. Python ofrece el bucle while y el for.

""" Bucle while """

# Usamos la palabra reservada "while" para hacer un bucle while. Es usado para ejecutar un bloque de declaraciones repetidas hasta que una condición
# se satisfaga. Cuando la condición se vuelve falsa, continúa el script con las siguientes líneas de código.

x = 0

while x < 10:
    x = x + 1
    if x == 5:
        break
    print(x)

print("Terminó de repetirse el bucle while.")


# Con la palabra reservada break nos salimos del bucle