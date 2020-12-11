#Autor : Sergio Roa
#Carrera: Ingeneria Informática

Cada elemento de este diccionario contiene una posicion y como valor tiene
el nombre de su elemento padre en el arbol

                  a
               /  |  \
              b   c   d
             / \  |  / \
            e   f h i   j
            |   | |     |
            k   m g     l
               / \
              n   o
"""
valores={
    "b":"a",
    "c":"a",
    "d":"a",
    "e":"b",
    "f":"b",
    "h":"c",
    "i":"d",
    "j":"d",
    "k":"e",
    "m":"f",
    "g":"h",
    "l":"j",
    "n":"m",
    "o":"m"
}
 
# variable que contiene el camino recorrido hasta llegar a la letra a buscar
camino=[]
 
def buscar(inicio,valorBuscar):
    """
    Funcion recursiva para buscar en profundidad
    Tiene que recibir:
        - el valor inicial donde empezar a buscar
        - el valor a buscar en su estructura
    Devuelve el valor a buscar o 0 si no lo encuentra
    """
    camino.append(inicio)
 
    # si encontramos el elemento, lo devolvemos
    if inicio==valorBuscar:
        return valorBuscar
 
    # recorremos todos los elementos en busca del valor de inicio
    for k,v in valores.items():
 
        # si el valor del elemento tiene como padre al valor de inicio
        if v==inicio:
 
            # llamamos a la función recursivamente enviando el nuevo padre
            result=buscar(k,valorBuscar)
 
            # si hemos recibido algun resultado es que hemos encontrado el
            # elemento que buscamos
            if result:
                return result
 
    camino.pop()
 
    # si llegamos aqui, es que hemos llegado al final de una profundidad
    return 0
 
result=buscar("a","o")
if result:
    print(camino)
else:
    print("no encontrado")
