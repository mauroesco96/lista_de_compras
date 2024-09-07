
lista_compras = []


while True:

    print("\nMenú de Opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")
    
    
    opcion = input("Elige una opción (1/2/3/4): ")
    
    if opcion == "1":
        
        articulo = input("Ingrese el nombre del artículo a agregar: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    
    elif opcion == "2":
       
        if lista_compras:
           
            print("Lista de compras actual:")
            for idx, item in enumerate(lista_compras):
                print(f"{idx}. {item}")
            
            
            try:
                indice = int(input("Ingrese el índice del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"Artículo '{eliminado}' eliminado de la lista.")
                else:
                    print("Índice no válido. Inténtelo de nuevo.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
        else:
            print("La lista de compras está vacía.")
    
    elif opcion == "3":
       
        if lista_compras:
            print("Lista de compras:")
            for item in lista_compras:
                print(f"- {item}")
        else:
            print("La lista de compras está vacía.")
    
    elif opcion == "4":
        
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
       
        print("Opción no válida. Inténtelo de nuevo.")
