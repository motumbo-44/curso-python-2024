"""Calculadora con bucles"""

print("""Bienvenido a la calculadora.
Esta le permite introducir un número, seleccionar una operación e introducir un segundo número.
Para salir escriba Salir.
Las opciones de operaciones son: suma, multi, resta y div.
Tome en cuenta que su resultado obtenido se almacenará como el primer número en una sugiente operación.
""")

resultado = ""
while True:
    if not resultado:
        resultado = input("Por favor, ingrese su número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("Por favor, ingrese la operación a llevar a cabo: ")
    if operacion.lower() == "salir":
        break
    numero2 = input("Por favor, ingrese su siguiente número: ")
    if numero2.lower() == "salir":
        break
    numero2 = int(numero2)

    if operacion.lower() == "suma":
        resultado += numero2
    elif operacion.lower() == "resta":
        resultado -= numero2
    elif operacion.lower() == "multi":
        resultado *= numero2
    elif operacion.lower() == "div":
        resultado /= numero2
    else:
        print("Por favor, ingrese una operación válida.")
        break

    print(f"El resultado de su operación es {resultado}")
