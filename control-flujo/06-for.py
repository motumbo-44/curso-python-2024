buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado el", buscar)
        break
else:
    print("No encontrado el", buscar)

for char in "Ultimate Python":
    print(char)
