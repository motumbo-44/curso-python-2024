n1 = input("Ingrese su primer número: ")
n2 = input("Ingrese su segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multip = n1 * n2
div = n1 / n2

mensaje = f"""
De los números dados {n1} y {n2}:
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicación es {multip}.
El resultado de la división es {div}.
"""

print(mensaje)
