""" countries = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": ["English", "Pashto", "Uzbek", "Turkmen"],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani",
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": ["Swedish"],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro",
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": ["English", "Albanian"],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek",
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": ["Arabic"],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar",
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": ["English", "Samoan"],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar",
    },
] """

# 1. Imprimir los idiomas del país Albania.
# print(countries[2]["languages"])

# 2. Imprimir el último idioma de Afghanistan y de American Samoa.
# print(countries[0]["languages"][-1])
# print(countries[-1]["languages"][-1])

# 3. Imprimir la mayor población. Identificar el país de esa población.
# nombre = " "
# cantidad = 0
# for dicti in countries:
# if dicti["population"] > cantidad:
# cantidad = dicti["population"]
# nombre = dicti["name"]

# print(nombre, ":", cantidad)

# 4. Imprimir los países que tengan como idioma el inglés.
# lo_tiene = []
# for dicti in countries:
# if "English" in dicti["languages"]:
# lo_tiene.append(dicti["name"])
# print(lo_tiene)

# nums = [1, 2, 3]
# new_lista = []

# for ele in nums:
# new_lista.append(ele + 1)

# print(new_lista)
# lo_tiene = []
# for dicti in countries:
# nombre = dicti["name"]
# lista = list(nombre)
# if lista[-1] == "s":
# print(dicti["name"])
# lo_tiene.append(dicti["name"])
# print(lo_tiene)

