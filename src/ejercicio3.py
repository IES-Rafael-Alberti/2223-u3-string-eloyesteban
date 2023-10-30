"""
Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""


def cuenta(cadena, letra_a_buscar):
    contador = 0
    for caracter in cadena:
        if caracter == letra_a_buscar:
            contador = contador + 1
    return contador

if __name__ == "__main__":

    cadena = 'banana'
    letra_a_buscar = 'a'
    resultado = cuenta(cadena, letra_a_buscar)
    print(resultado)  
