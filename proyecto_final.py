items1 = {
    "Carnes": ["Pescado", "Cerdo", "Pollo"],
    "Tarifas": {"Normal": 100},
}

items2 = {
    "Verduras": ("Lechuga", "Tomate", "Cebolla"),
    True: ["Fria", "Caliente"],
    "Tarifas": [40],
}

items3 = {
    "Bebidas": [
        "Gaseosa",
        "Jugo de Mora",
        "Jugo de Lulo",
        "Jugo de Naranja",
        "Jugo de Piña",
    ],
    "Tamaño": [250, 300, 350],
    "Tarifas": [25],
}

items4 = {"Adiciones": ["Guacamole", "Ají", "Chimichurry", "Vinagreta", 15]}


def seleccionar_carnes():
    carnes = items1["Carnes"]
    tarifas = items1["Tarifas"]
    print("------SELECCIONAR CARNES------")
    print(
        "Seleciona mínimo dos carnes o 'Saltar' para omitir con recargo (150 + tarifa normal)"
    )
    contador = 1
    for carne in carnes:
        print(f"{contador}. {carne} ($100)")
        contador = contador + 1
    # Por ahora esto imprime:
    # 1. Pescado
    # 2. Cerdo
    # 3. Pollo
    seleccionar = input("Ingrese la primera opción (ej: 1) o 'Saltar': ").lower()
    carnes_seleccionadas = []
    total_carnes = 0
    if seleccionar == "saltar":
        recargo = 150 + tarifas["Normal"]  # 250
        print(f"Selección omitida. Se cobró 150 + tarifa normal = ${recargo}")
        carnes_seleccionadas.append("No seleccionó carnes")
        total_carnes = recargo
    else:
        while True:  # Lo cambiaremos a True y lo cerramos con break
            if seleccionar == "1":
                print("Pescado seleccionado")
                total_carnes = total_carnes + tarifas["Normal"]
                carnes_seleccionadas.append(carnes[0])
            elif seleccionar == "2":
                print("Cerdo seleccionado")
                total_carnes = total_carnes + tarifas["Normal"]
                carnes_seleccionadas.append(carnes[1])
            elif seleccionar == "3":
                print("Pollo seleccionado")
                total_carnes = total_carnes + tarifas["Normal"]
                carnes_seleccionadas.append(carnes[2])
            elif seleccionar == "continuar":
                if len(carnes_seleccionadas) >= 2:
                    break
                else:
                    print("Selecciona al menos dos carnes para continuar ")
            contador = 1
            for carne in carnes:
                print(f"{contador}. {carne} ($100)")
                contador = contador + 1
            seleccionar = input(
                "Ingrese otra opción (ej: 1) o 'continuar' si no quiere más opciones: "
            ).lower()

    print(f"Carnes seleccionadas: {carnes_seleccionadas}. Total: {total_carnes}")
    return carnes_seleccionadas, total_carnes


def seleccionar_temp(temp):
    temperatura = items2[True]
    if temperatura[0].lower() == temp:
        return "Fria"
    else:
        return "Caliente"


def seleccionar_verduras():
    verduras = items2["Verduras"]
    tarifas1 = items2["Tarifas"]
    print("------SELECCIONAR VERDURAS------")
    print(
        "Seleccionar mínimo dos verduras o 'Saltar' para omitir con recargo (150 + tarifa normal)"
    )
    contador = 1
    for verdura in verduras:
        print(f"{contador}. {verdura} ($40)")
        contador = contador + 1
    seleccionar = input("Ingrese la primera opción (ej 1, 2 o 3) o 'Saltar': ").lower()
    verduras_seleccionadas = []
    total_verduras = 0
    if seleccionar == "saltar":
        recargo = 150 + tarifas1[0]
        print(f"Selección omitida. Se cobró 150 + tarifa normal = ${recargo}")
        verduras_seleccionadas.append("No seleccionó verduras")
        total_verduras = recargo
    else:
        while True:
            if seleccionar == "1":
                print("Lechuga seleccionada")
                total_verduras = total_verduras + tarifas1[0]
                presentacion = input("Escoja la temperatura deseada (fria, caliente): ")
                temp = seleccionar_temp(presentacion)
                verduras_seleccionadas.append([verduras[0], temp])
            elif seleccionar == "2":
                print("Tomate seleccionado")
                total_verduras = total_verduras + tarifas1[0]
                presentacion = input("Escoja la temperatura deseada (fria, caliente): ")
                temp = seleccionar_temp(presentacion)
                verduras_seleccionadas.append([verduras[1], temp])
            elif seleccionar == "3":
                print("Cebolla seleccionada")
                total_verduras = total_verduras + tarifas1[0]
                presentacion = input("Escoja la temperatura deseada (fria, caliente): ")
                temp = seleccionar_temp(presentacion)
                verduras_seleccionadas.append([verduras[2], temp])
            elif seleccionar == "continuar":
                if len(verduras_seleccionadas) >= 2:
                    break
                else:
                    print("Selecciona al menos dos verduras para continuar")
            contador = 1
            for verdura in verduras:
                print(f"{contador}. {verdura} ($40)")
                contador = contador + 1
            seleccionar = input(
                "Ingrese otra opción (ej: 1, 2 o 3) o 'continuar' si no quiere más opciones: "
            ).lower()

    print(f"Verduras seleccionadas: {verduras_seleccionadas}. Total: {total_verduras}")
    return verduras_seleccionadas, total_verduras


def seleccionar_pre(pres):
    presentacion = items3["Tamaño"]
    if presentacion[0] == pres:
        return "250"
    elif presentacion[1] == pres:
        return "300"
    else:
        return "350"


def seleccionar_bebidas():
    bebidas = items3["Bebidas"]
    tarifas2 = items3["Tarifas"]
    print("------SELECCIONAR BEBIDAS------")
    print(
        "Seleccionar mínimo dos bebidas o 'Saltar' para omitir con recargo (150 + tarifa normal)"
    )
    contador = 1
    for bebida in bebidas:
        print(f"{contador}. {bebida} ($25)")
        contador = contador + 1
    seleccionar = input(
        "Ingrese la primera opción (ej 1,2,3,4 o 5) o 'Saltar':"
    ).lower()
    bebidas_seleccionadas = []
    total_bebidas = 0
    if seleccionar == "saltar":
        recargo = 150 + tarifas2[0]
        print(f"Selección omitida. Se cobró 150 + tarifa normal = ${recargo}")
        bebidas_seleccionadas.append("No seleccionó bebida")
        total_bebidas = recargo
    else:
        while True:
            if seleccionar == "1":
                print("Gaseosa selecionada")
                total_bebidas = total_bebidas + tarifas2[0]
                presentacion = int(input("Escoja la presentación: (250, 300, 350): "))
                pre = seleccionar_pre(presentacion)
                bebidas_seleccionadas.append([bebidas[0], pre])
            elif seleccionar == "2":
                print("Jugo de Mora seleccionado")
                total_bebidas = total_bebidas + tarifas2[0]
                presentacion = int(input("Escoja la presentación: (250, 300, 350): "))
                pre = seleccionar_pre(presentacion)
                bebidas_seleccionadas.append([bebidas[1], pre])
            elif seleccionar == "3":
                print("Jugo de Lulo seleccionado")
                total_bebidas = total_bebidas + tarifas2[0]
                presentacion = int(input("Escoja la presentación: (250, 300, 350): "))
                pre = seleccionar_pre(presentacion)
                bebidas_seleccionadas.append([bebidas[2], pre])
            elif seleccionar == "4":
                print("Jugo de Naranja seleccionado")
                total_bebidas = total_bebidas + tarifas2[0]
                presentacion = int(input("Escoja la presentación: (250, 300, 350): "))
                pre = seleccionar_pre(presentacion)
                bebidas_seleccionadas.append([bebidas[3], pre])
            elif seleccionar == "5":
                print("Jugo de Piña seleccionado")
                total_bebidas = total_bebidas + tarifas2[0]
                presentacion = int(input("Escoja la presentación: (250, 300, 350): "))
                pre = seleccionar_pre(presentacion)
                bebidas_seleccionadas.append([bebidas[4], pre])
            elif seleccionar == "continuar":
                if len(bebidas_seleccionadas) >= 2:
                    break
                else:
                    print("Selecciona al menos dos bebidas para continuar")
            contador = 1
            for bebida in bebidas:
                print(f"{contador}. {bebida} ($25)")
                contador = contador + 1
            seleccionar = input(
                "Ingrese otra opción (ej: 1,2,3,4 o 5) o 'continuar' si no quiere más opciones: "
            ).lower()
    print(f"Bebidas seleccionadas: {bebidas_seleccionadas}. Total: {total_bebidas}")
    return bebidas_seleccionadas, total_bebidas


def seleccionar_adiciones():
    adiciones = items4["Adiciones"][:4]
    tarifa4 = items4["Adiciones"][-1]
    print("------SELECCIONAR ADICIONES------")
    print(
        "Seleccionar mínimo dos adiciones o 'Saltar' para omitir con recargo (150 + tarifa normal)"
    )
    contador = 1
    for adicion in adiciones:
        print(f"{contador}. {adicion} ($15)")
        contador = contador + 1
    seleccionar = input(
        "Ingrese la primera opción (ej 1, 2, 3 o 4) o 'Saltar': "
    ).lower()
    adiciones_seleccionadas = []
    total_adiciones = 0
    if seleccionar == "saltar":
        recargo = 150 + tarifa4
        print(f"Selección omitida. Se cobró 150 + tarifa normal = ${recargo}")
        adiciones_seleccionadas.append("No seleccionó adición")
        total_adiciones = recargo
    else:
        while True:
            if seleccionar == "1":
                print("Guacamole seleccionado")
                total_adiciones = total_adiciones + tarifa4
                adiciones_seleccionadas.append(adiciones[0])
            elif seleccionar == "2":
                print("Ají seleccionado")
                total_adiciones = total_adiciones + tarifa4
                adiciones_seleccionadas.append(adiciones[1])
            elif seleccionar == "3":
                print("Chimichurry seleccionado")
                total_adiciones = total_adiciones + tarifa4
                adiciones_seleccionadas.append(adiciones[2])
            elif seleccionar == "4":
                print("Vinagreta seleccionada")
                total_adiciones = total_adiciones + tarifa4
                adiciones_seleccionadas.append(adiciones[3])
            elif seleccionar == "continuar":
                if len(adiciones_seleccionadas) >= 2:
                    break
                else:
                    print("Selecciona al menos dos adiciones para continuar")
            contador = 1
            for adicion in adiciones:
                print(f"{contador}. {adicion} ($15)")
                contador = contador + 1
            seleccionar = input(
                "Ingrese otra opción (ej: 1, 2, 3 o 4) o 'continuar' si no quiere más opciones: "
            ).lower()
    print(
        f"Adiciones seleccionadas: {adiciones_seleccionadas}. Total: {total_adiciones}"
    )
    return adiciones_seleccionadas, total_adiciones


def num2word(numero):
    unidades = [
        "cero",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    especiales = [
        "diez",
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    ]
    decenas = [
        "",
        "",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    centenas = [
        "",
        "ciento",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]

    if numero < 10:
        return unidades[numero]
    if numero < 20:
        return especiales[numero - 10]
    if numero < 100:
        dec = numero // 10
        uni = numero % 10
        if dec == 2 and uni > 0:
            return "veinti" + unidades[uni]
        if uni == 0:
            return decenas[dec]
        return decenas[dec] + " y " + unidades[uni]
    if numero == 100:
        return "cien"
    if numero < 1000:
        cent = numero // 100
        resto = numero % 100
        if resto == 0:
            return "cien" if cent == 1 else centenas[cent]
        return centenas[cent] + " " + num2word(resto)
    if numero < 1000000:
        miles = numero // 1000
        resto = numero % 1000

        if miles == 1:
            miles_texto = "mil"
        else:
            miles_texto = num2word(miles) + " mil"

        if resto == 0:
            return miles_texto
        return miles_texto + " " + num2word(resto)

    return "El número no está dentro del rango."


carnes, total_c = seleccionar_carnes()
verduras, total_v = seleccionar_verduras()
bebidas, total_b = seleccionar_bebidas()
adiciones, total_a = seleccionar_adiciones()

total_pedido = total_c + total_v + total_b + total_a
total_general = {
    "Carnes": carnes,
    "Verduras": verduras,
    "Bebidas": bebidas,
    "Adiciones": adiciones,
    "Total": f"${total_pedido} ({num2word(total_pedido)} pesos)",
}

print("\n----RESUMEN DEL PEDIDO----")
for categoria, items in total_general.items():
    print(f"{categoria}: {items}")
