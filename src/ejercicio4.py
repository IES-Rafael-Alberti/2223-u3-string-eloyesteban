def contar_apariciones(palabra, letra):
    return palabra.count(letra)

if __name__ == "__main__":

    palabra = "banana"
    letra = "a"
    resultado = contar_apariciones(palabra, letra)
    print("La letra '" + str(letra) + "' aparece " + str(resultado) + " veces en " + str(palabra))
