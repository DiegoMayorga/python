items1 = {
    "Carnes": {"Pescado", "Cerdo", "Pollo"},
    "Precio": 100,
}
items2 = {
    "Verduras": ["Lechuga", "Tomate", "Cebolla"],
    True: ["Fria", "Caliente"],
    "Precio": 40,
}

items3 = {
    "Bebidas": "Gaseosa",
    "Presentación": 250,
    "Jugos": ("Lulo", "Mora", "Naranja", "Piña"),
    "Precio": 25,
}

items4 = {
    "Adiciones": ["Guacamole", "Aji", "Chimichurry", "Vinagreta", (20, 15, 10, 8)]
}

"""
========== CARNES =============
Carnes:
Pescado - 100
Cerdo - 100
Pollo - 100
========== VERDURAS =============
Verduras:
Lechuga - 40
Tomate - 40
Cebolla - 40
Opciones: 
Fria - Caliente
========== BEBIDAS =============
Bebidas:
Gaseosa 250ml - 25
Jugos (Lulo, Mora, Naranja, Piña) 250ml - 25
========== ADICIONES =============
Adiciones:
Guacamole - 20
Aji - 15
Chimichurry - 10
Vinagreta - 8
"""


def mostrar_menu():
    print("Bienvenido! Este es nuestro Menu: ")

    print("============CARNES==========")
    # items 1
    precio_carnes = items1["Precio"]
    for dicti_carnes in items1:
        if items1[dicti_carnes] == items1["Carnes"]:
            for carne in items1["Carnes"]:
                print(f"{carne} - ${precio_carnes}")

    print("==========VERDURAS==========")
    # items 2
    for verdura in items2["Verduras"]:
        print(f"{verdura} - ${items2["Precio"]}")
    print("Presentación:")
    for temp in items2[True]:
        print(temp)

    print("==========BEBIDAS==========")
    # items 3
    print(f"{items3["Bebidas"]} - {items3["Presentación"]}mL - ${items3["Precio"]}")
    lista_jugos = list(items3["Jugos"])
    print(
        f"Jugos ({", ".join(lista_jugos)}) - {items3["Presentación"]}mL - ${items3["Precio"]}"
    )

    print("==========ADICIONES==========")
    # items 4
    adiciones = items4["Adiciones"]
    print(f"{adiciones[0]} - ${adiciones[-1][0]}")
    print(f"{adiciones[1]} - ${adiciones[-1][1]}")
    print(f"{adiciones[2]} - ${adiciones[-1][2]}")
    print(f"{adiciones[3]} - ${adiciones[-1][3]}")


mostrar_menu()
continuar = int(input("Presione 1 para continuar"))
while continuar != 1:
    print("Tecla equivocada, intente nuevamente")
    continuar = int(input("Presione 1 para continuar "))


def mostrar_carnes():
    precio_carnes = items1["Precio"]
    numero = 1
    for dicti_carnes in items1:
        if items1[dicti_carnes] == items1["Carnes"]:
            nueva_lista = list(items1["Carnes"])
            lista_ordenada = sorted(nueva_lista)
            for carne in lista_ordenada:
                print(f"{numero}. {carne} - ${precio_carnes}")
                numero = numero + 1


def mostrar_verduras():
    numero = 1
    for verdura in items2["Verduras"]:
        print(f"{numero}. {verdura} - ${items2["Precio"]}")
        numero = numero + 1


def mostrar_temp():
    print("Presentación:")
    numero = 1
    for temp in items2[True]:
        print(f"{numero}. {temp}")
        numero = numero + 1


def mostrar_bebidas():
    print(f"{items3["Bebidas"]} - {items3["Presentación"]}mL - ${items3["Precio"]}")
    lista_jugos = list(items3["Jugos"])
    print(
        f"Jugos ({", ".join(lista_jugos)}) - {items3["Presentación"]}mL - ${items3["Precio"]}"
    )


def mostrar_adiciones():
    adiciones = items4["Adiciones"]
    print(f"{adiciones[0]} - ${adiciones[-1][0]}")
    print(f"{adiciones[1]} - ${adiciones[-1][1]}")
    print(f"{adiciones[2]} - ${adiciones[-1][2]}")
    print(f"{adiciones[3]} - ${adiciones[-1][3]}")


compra = []
carnes = []
print("Selecciona dos opciones")
mostrar_carnes()

opcion1_carnes = int(input("Seleccione una opción "))

if opcion1_carnes == 1:
    print("Cerdo seleccionado")
    carnes.append("Cerdo")
elif opcion1_carnes == 2:
    print("Pescado seleccionado")
    carnes.append("Pescado")
elif opcion1_carnes == 3:
    print("Pollo seleccionado")
    carnes.append("Pollo")
else:
    print("Selecciona un número válido")

mostrar_carnes()
opcion2_carnes = int(input("Seleccione otra opción "))

if opcion2_carnes == 1:
    print("Cerdo seleccionado")
    carnes.append("Cerdo")
elif opcion2_carnes == 2:
    print("Pescado seleccionado")
    carnes.append("Pescado")
elif opcion2_carnes == 3:
    print("Pollo seleccionado")
    carnes.append("Pollo")
else:
    print("Selecciona un número válido")

verduras = []
print("Selecciona dos opciones")
mostrar_verduras()
opcion1_verduras = int(input("Seleccione una opción "))
if opcion1_verduras == 1:
    print("Lechuga seleccionado")
    verduras.append("Lechuga")
elif opcion1_verduras == 2:
    print("Tomate seleccionado")
    verduras.append("Tomate")
elif opcion1_verduras == 3:
    print("Cebolla seleccionado")
    verduras.append("Cebolla")
else:
    print("Selecciona un número válido")

mostrar_verduras()
opcion2_verduras = int(input("Seleccione una opción "))
if opcion2_verduras == 1:
    print("Lechuga seleccionado")
    verduras.append("Lechuga")
elif opcion2_verduras == 2:
    print("Tomate seleccionado")
    verduras.append("Tomate")
elif opcion2_verduras == 3:
    print("Cebolla seleccionado")
    verduras.append("Cebolla")
else:
    print("Selecciona un número válido")

print(
    f"Resumen del pedido:\n Carnes: {", ".join(carnes)}\n Verduras: {", ".join(verduras)}"
)
