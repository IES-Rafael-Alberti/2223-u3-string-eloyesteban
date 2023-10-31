"""
Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]? 
"""

fruta = input("Introduce una fruta: ")

print(fruta[:])


"""
Si fruta es una variable de tipo cadena, entonces fruta[:] es una notación que se refiere a una "rebanada" (o "slice") de la cadena. En Python, las cadenas (y otros tipos de secuencias, como listas) pueden ser "rebanadas" para obtener subsecuencias.

La notación fruta[:] toma todos los caracteres de la cadena desde el principio hasta el final. Por lo tanto, es esencialmente una forma de crear una copia de la cadena original. 
"""
