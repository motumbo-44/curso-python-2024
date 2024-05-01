def no_espacio(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_alreves = ""
    for char in texto:
        texto_alreves = char + texto_alreves
    return texto_alreves


def es_palindromo(texto):
    texto = no_espacio(texto)
    texto_alreves = reverse(texto)
    return texto.lower() == texto_alreves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("hola mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Somos o no somos"))
print(es_palindromo("Somos o te haces"))
