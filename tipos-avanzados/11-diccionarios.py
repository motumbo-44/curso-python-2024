punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)
if "lala" in punto:
    print("Se encontró lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 44))

del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(valor)

usuarios = [
    {"id": 1, "nombre": "Nadia"},
    {"id": 2, "nombre": "Mario"},
    {"id": 1, "nombre": "Esteban"},
    {"id": 1, "nombre": "Luis"}
]

for usuario in usuarios:
    print(usuario["nombre"])
