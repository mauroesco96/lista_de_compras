# lista_de_compras
Evaluación de desempeño (60%)
Objetivo: Crear una aplicación en Python que gestione una lista de compras, permitiendo agregar, eliminar y mostrar los artículos.

Pasos:

1. Crear un repositorio en GitHub:

Crea un nuevo repositorio llamado "lista_de_compras".
Inicializa el repositorio con un archivo README.md que describa el proyecto.

2. Crear un archivo Python:

Crea un archivo llamado lista_compras.py dentro de tu repositorio.

3. Inicializar la lista de compras:

Crea una variable llamada lista_compras como una lista vacía: lista_compras = []

4. Bucle principal:

Crea un bucle while que se ejecute hasta que el usuario decida salir.
Dentro del bucle:
Presenta al usuario un menú de opciones:
Agregar artículo
Eliminar artículo
Mostrar lista
Salir
Solicita al usuario que ingrese una opción usando input().

5. Manejar las opciones del menú:

Utiliza if, elif y else para manejar cada opción del menú:
Opción 1 (Agregar artículo):
Solicita al usuario el nombre del artículo usando input().
Agrega el artículo a la lista lista_compras usando append().
Opción 2 (Eliminar artículo):
Muestra la lista de compras actual.
Solicita al usuario el índice del artículo a eliminar usando input().
Convierte la entrada a un entero usando int().
Elimina el artículo de la lista usando del lista_compras[índice].
Opción 3 (Mostrar lista):
Imprime la lista de compras usando print().
Opción 4 (Salir):
Imprime un mensaje de despedida y termina el bucle.

6. Subir los cambios al repositorio:

Agrega los cambios realizados al archivo lista_compras.py al stage del Git: git add .
Crea un commit con un mensaje descriptivo: git commit -m "Implementación inicial de la lista de compras"
Sube los cambios al repositorio remoto: git push origin main