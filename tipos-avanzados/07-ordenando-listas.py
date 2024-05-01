numeros = [4, 3, 1, 2, 5, 6]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
