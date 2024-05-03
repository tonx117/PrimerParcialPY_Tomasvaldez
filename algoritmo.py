
lista = [1, 2, 3, 4, 4, 5, 6, 6, 7]

def eliminar_duplicados (list):
    
    # se crea una variable llamada list que recibe la lista sin repetidos en forma de objeto
    list = list(set(lista))
    
    print(list)
    
eliminar_duplicados(list)

