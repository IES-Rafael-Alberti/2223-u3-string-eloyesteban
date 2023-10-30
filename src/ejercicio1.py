"""
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente. 
"""

def invertir_cadena(cadena):
    resultado = []
    indice = len(cadena) - 1
    while indice >= 0:
        resultado.append(cadena[indice])
        indice -= 1
    return resultado

if __name__ == "__main__":

    #Entrada

    cadena = input("Introduce una cadena: ")

    #Procesar

    cadena_invertida = invertir_cadena(cadena)

    #Salida

    for char in cadena_invertida:
        print(char)