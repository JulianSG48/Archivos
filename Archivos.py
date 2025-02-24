import csv

archivo_csv = "SalesJan2009.csv"

pais_buscado = input("Ingrese el pais a consultar: ")

contador = 0

with open(archivo_csv,"r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezados = next(lector) 

    indice_pais = encabezados.index("Country")

    for fila in lector:
        if fila[indice_pais] == pais_buscado:
            contador += 1

print(f"Compras en {pais_buscado}: {contador}")
