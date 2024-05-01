usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# map (comprension de listas)
# nombres = [usuario[0] for usuario in usuarios]

# filter (comprension de listas)
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# map + filter (comprension de listas)
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# map
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
