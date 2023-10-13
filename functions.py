'''
Funciones y diccionario
Registro y Consulta de estudiantes Universitarios

Sebastián Alzate Sierra
Maria Paula Ramos
Juan Isaza

Taller #2 Programación
'''
#____________________________________________________________________________________________________________________
#Crear diccionario para base de datos.
#Clave - etiqueta de diccionario estudiantes : Nombre
#Diccionario de datos : datos
estudiantes = {} 

#Crear diccionario para las carreras
#Clave - etiqueta de diccionario carreras : Número
#Diccionario de datos : Nombre de la carrera
carreras = { 
    "1": "Ingeniería de Productividad y Calidad",
    "2": "Ingeniería Agropecuaria",
    "3": "Ingeniería civil",
    "4": "Ingeniería en seguridad y salud en el trabajo",
    "5": "Ingeniería en Automatización y control",
    "6": "Ingeniería informática"
}
#____________________________________________________________________________________________________________________________________________
def load_data():
    '''
    Carga base de datos
    En caso de exitir se carga, de lo contrario comienza una nueva base de datos vacía
    '''
    try: 
        with open("base_de_datos.txt", "r") as archivo: #Lectura de base de datos, se usa with porque este cierra la base de datos cuando acaba el bloque with
            for linea in archivo:                       #Iteración linea por linea del archivo
                cedula, nombre, edad, carrera, promedio = linea.strip().split(",")  #Cada dato es separado por ","
                edad = int(edad)                        #Cada edad es cargada como entero
                promedio = float(promedio)              #Cada promedio es cargado como flotante
                estudiantes[cedula] = {"nombre": nombre, "edad": edad, "carrera": carrera, "promedio": promedio}  #Clave: cedula , Dicc:nombre, edad, carrera, promedio
        print(f"Base de datos cargada con {len(estudiantes)} estudiantes.")                     #Cantidad de estudiantes previamente registrados
    except FileNotFoundError:                           #Si el archivo de base de datos no existe - no se encuentra
        print("No se encontró base de datos anterior, comenzando con una base de datos vacía.")
#______________________________________________________________________________________________________________________________________________        
def save_data():
    '''
    Guardar base de datos
    '''
    with open("base_de_datos.txt", "w") as archivo:     #Escritura en base de datos
        for cedula, datos in estudiantes.items():       # Recorrer diccionario estudiantes, para añadir clave y datos
            archivo.write(f"{cedula},{datos['nombre']},{datos['edad']},{datos['carrera']},{datos['promedio']}\n") #Escribir en cada linea la clave(cedula) , con sus datos
    print("Base de datos guardada.")
#________________________________________________________________________________________________________________________
def register():
    '''
    
    Registro de estudiantes
    
    '''
    while True:
        cedula = input("Ingrese la cedula del estudiante sin puntos y sin espacios: ")
        if cedula.isdigit():  
            break                                       #Salir del bucle si cumple la condición
        else:
            print("Error. Vuelva a ingresar la cedula.")

    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.isalpha():
            break
        else:
            print("Error: El nombre debe contener solo letras.")

    while True:
        edad = input("Ingrese la edad del estudiante: ")
        try:
            edad = int(edad)                            #Conversión a entero
            if 15 <= edad <= 90:                        #Rango edad
                break                                   #Salir del bucle si cumple la condición
            else:
                print("Error: La edad debe estar en el rango de 15 a 90 años")
        except ValueError:                              # Si la conversión a entero no funciona (No es entero)
            print("Error: La edad debe ser un número entero válido.")  

    while True:
        print("Seleccione una carrera de la siguiente lista:")
        print("1. Ingeniería de Productividad y Calidad")
        print("2. Ingeniería Agropecuaria")
        print("3. Ingeniería civil")
        print("4. Ingeniería en seguridad y salud en el trabajo")
        print("5. Ingeniería en Automatización y control")
        print("6. Ingeniería informática")
        opcion_carrera = input("Ingresar opción: ")

        if opcion_carrera in ("1", "2", "3", "4", "5", "6"):    #Validar opción existente
            break                                       #Salir del bucle si cumple la condición
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción válida.")

    while True:
        promedio = input("Ingrese el promedio del estudiante entre 0.0 y 5.0: ")
        try:
            promedio = float(promedio)                  #Conversión a flotante
            if 0.0 <= promedio <= 5.0:                  #Rango de notas posibles
                estudiantes[cedula] = {"nombre": nombre, "edad": edad, "carrera": opcion_carrera, "promedio": promedio} #Se dió registro exitoso, se guarda la clave cedula con un diccionario con sus datos
                print("Estudiante registrado exitosamente.")
                break                                   #Salir del bucle si cumple la condición
            else:
                print("Error: El promedio debe estar entre 0.0 y 5.0.")
        except ValueError:                              #Conversión a flotante falló (No es ni entero ni decimal)
            print("Error: El promedio debe ser un número decimal válido.")
#_____________________________________________________________________________________________________________________

def students_inquiry():
    '''
    Consulta de estudiantes pertenecientes de una carrera
    '''
    while True:  
        print("Carreras disponibles:")                   #Imprime un mensaje indicando que se mostrarán las carreras disponibles
        for numero, nombre_carrera in carreras.items():  #Itera a través de las carreras disponibles.
            print(f"{numero}. {nombre_carrera}")         #Imprime el número y nombre de cada carrera.

        opcion_carrera = input("Ingrese el número de la carrera a consultar: ")     #Solicita al usuario que ingrese el número de la carrera a consultar

        if opcion_carrera in carreras:                    #Verifica si la opción ingresada está en el diccionario de carreras
            estudiantes_carrera = filter(lambda x: x[1]["carrera"] == opcion_carrera, estudiantes.items()) #Filtra los estudiantes cuya carrera coincide con la opción ingresada
            #Filter , filtra los estudiantes.items(), toma dos argumentos , lambda(encargada del filtro) y el iterable (estudiantes.items())
            #Itera cada tupla en estudiantes.items() si es True (coinciden las carreras), se incluye el resultado
            estudiantes_carrera = list(estudiantes_carrera) #Convierte el filtro en una lista

            if len(estudiantes_carrera) > 0:        #Verifica existencia de estudiantes
                print(f"Estudiantes de la carrera {carreras[opcion_carrera]}:")     #Imprime el título con el nombre de la carrera
                for cedula, datos in estudiantes_carrera:   #Itera a través de los estudiantes encontrados
                    nombre = datos.get('nombre', 'Nombre no disponible')  # Usar 'get' para obtener el nombre
                    edad = datos.get('edad', 'Edad no disponible')        # Usar 'get' para obtener la edad
                    promedio = datos.get('promedio', 'Promedio no disponible')  # Usar 'get' para obtener el promedio
                    print(f"Cédula: {cedula}, Nombre: {datos['nombre']} , Edad: {datos['edad']}, Promedio: {datos['promedio']}")    #Imprime todo lo del estudiante
            else:
                print(f"No se encontraron estudiantes en la carrera {carreras[opcion_carrera]}.")
            break  # Salir del bucle si se ingresó una opción válida
        else:
            print("Error: Opción no válida. Por favor, ingrese un número de carrera válido.")


#______________________________________________________________________________________________________________________
def general_average():
    '''
    
    Promedio general de todos los estudiantes
    
    '''
    if len(estudiantes) > 0:
        
        estudiantes_con_promedio = [estudiante for estudiante in estudiantes.values() if 'promedio' in estudiante]  # Tomar todos los registros que tengan la palabra promedio en la base de datos
        
        if len(estudiantes_con_promedio) > 0:           #Validar que existan registros previos.
            promedio_general = sum(estudiante['promedio'] for estudiante in estudiantes_con_promedio) / len(estudiantes_con_promedio)   #Cálculo del promedio
            #Recorre cada estudiante del diccionario, que esté en estudiantes_con_promedio y obtiene el valor del promedio
            #lo suma con la función sum y lo divide por la cantidad de estudiantes de registrados
        
            print(f"Promedio general de todos los estudiantes: {promedio_general:.2f}")
        else:
            print("No hay estudiantes con promedio registrado.")
    else:
        print("No hay estudiantes registrados.")

#___________________________________________________________________________________________________________________________
def best_students():
    '''
    Estudiantes destacados
    '''
    try:
        estudiantes_destacados = list(filter(lambda x: "promedio" in x[1] and x[1]["promedio"] >= 4.5, estudiantes.items()))
        #Comprueba si promedio está en los items (el segundo elemento de la tupla o sea los datos, el primero es la clave)
        #verifica que el valor sea mayor a 4.5
        #Convierte el filter en una lista
        
        if len(estudiantes_destacados) > 0:     #Corrobora la existencia de estudiantes
            print("Estudiantes destacados:")
            for cedula, datos in estudiantes_destacados:     #Mostrar detalles de los estudiantes destacados
                nombre = datos.get('nombre', 'Nombre no disponible')  # Usar 'get' para obtener el nombre o proporcionar un valor predeterminado
                edad = datos.get('edad', 'Edad no disponible')        # Usar 'get' para obtener la edad o proporcionar un valor predeterminado
                promedio = datos.get('promedio', 'Promedio no disponible')  # Usar 'get' para obtener el promedio o proporcionar un valor predeterminado
                print(f"Cédula: {cedula}, Nombre: {datos['nombre']}, Edad: {datos['edad']}, Carrera: {datos['carrera']}, Promedio: {datos['promedio']}")
        else:
                print("No hay estudiantes destacados.")
    except TypeError:
        print("No hay estudiantes registrados.")


#___________________________________________________________________________________________________________________________
def best_students_by_career():
    '''
    Estudiantes destacados por carrera
    '''
    while True:                                  #Este bucle se ejecutará hasta que se ingrese una opción válida.
        print("Carreras disponibles:")
        
        for numero, nombre_carrera in carreras.items(): #Itera sobre el diccionario de carreras e imprime el nombre y número de cada carrera.
            print(f"{numero}. {nombre_carrera}")
        
        opcion_carrera = input("Ingrese el número de la carrera a consultar: ") 
        if opcion_carrera in carreras:      # Verifica si la opción ingresada por el usuario está en el diccionario de carreras.
            
            estudiantes_destacados = list(filter(lambda x: "promedio" in x[1] and x[1]["promedio"] >= 4.5 and x[1]["carrera"] == opcion_carrera, estudiantes.items()))
            #Filtra estudiantes destacados en la carrera seleccionada y los almacena en estudiantes_destacados.
            #Comprueba si promedio está en los items (el segundo elemento de la tupla o sea los datos, el primero es la clave).
            #Verifica que el valor sea mayor a 4.5 y que la carrera seleccionada sea igual a una existente (de 1 a 6).
            
            if len(estudiantes_destacados) > 0: #Verifica si hay estudiantes destacados en la carrera.                
                print(f"Estudiantes destacados en la carrera {carreras[opcion_carrera]}:") # Imprime el título de la carrera y luego los datos de los estudiantes destacados.
                for cedula, datos in estudiantes_destacados:
                    nombre = datos.get('nombre', 'Nombre no disponible')  # Usar 'get' para obtener el nombre
                    edad = datos.get('edad', 'Edad no disponible')        # Usar 'get' para obtener la edad
                    promedio = datos.get('promedio', 'Promedio no disponible')  # Usar 'get' para obtener el promedio
                    print(f"Cédula: {cedula}, Nombre: {datos['nombre']}, Edad: {datos['edad']}, Promedio: {datos['promedio']}")
                break                           #Sale del bucle while cuando se muestra la información.
            else:                
                print(f"No se encontraron estudiantes destacados en la carrera {carreras[opcion_carrera]}.")
                break                           #Sale del bucle while ya que se manejó la opción válida.
        else:
            print("Error: Opción no válida. Por favor, ingrese un número de carrera válido.")


#___________________________________________________________________________________________________________________________
def update_students():
    '''
    Actualización de la información de los estudiantes
    '''

    if len(estudiantes) > 0:                       #Verifica si hay estudiantes.
        print("Lista de Estudiantes:")             #Mostrar la lista de estudiantes con un número de identificación
        i = 1                                      #Inicializamos i en 1 para llevar un número de identificación.
        for cedula, datos in estudiantes.items():  #Iteramos a través de los estudiantes y sus datos.
            nombre_carrera = carreras[datos['carrera']]  #Obtenemos el nombre de la carrera a partir del código de carrera.
            
            print(f"{i}. Cédula: {cedula}, Nombre: {datos['nombre']}, Edad: {datos['edad']}, Carrera: {nombre_carrera}, Promedio: {datos['promedio']}")
            i += 1                                 #Incrementamos i para el siguiente estudiante.

        while True:                                 #Iniciamos un bucle infinito para la interacción del usuario.
            try:
                seleccion = int(input("Ingrese el número del estudiante a actualizar: "))  #Solicitamos al usuario que ingrese un número.

                if 1 <= seleccion <= len(estudiantes):
                    cedula_estudiante = list(estudiantes.keys())[seleccion - 1]
                    estudiante = estudiantes[cedula_estudiante]
                    
                    # Nueva carrera
                    print("Seleccione la nueva carrera: ")
                    for numero, nombre_carrera in carreras.items():     #Iteramos a través de las carreras.
                        print(f"{numero}. {nombre_carrera}")            #Mostramos las opciones de carrera.

                    while True:                                         #Bucle para la selección de carrera.
                        opcion_carrera = input("Seleccione la nueva carrera: ")  #Solicitamos al usuario que seleccione una carrera.
                        if opcion_carrera in carreras:                           #Verificamos si la opción es válida.
                            estudiante["carrera"] = opcion_carrera               #Actualizamos la carrera del estudiante.
                            break                                                #Salimos del bucle de selección de carrera.
                        else:
                            print("Seleccione una opción válida.")               # Mensaje de error en caso de selección no válida.

                    # Edad nueva
                    while True:                                                    # Bucle para la entrada de la nueva edad.
                        edad_actualizada = input("Ingrese la nueva edad: ")        # Solicitamos al usuario que ingrese la nueva edad.
                        if edad_actualizada.isdigit():                             # Verificamos si la entrada es un número.
                            edad_actualizada = int(edad_actualizada)               # Convertimos la entrada a entero.
                            if 15 <= edad_actualizada <= 90:                       # Verificamos si la edad está en el rango válido.
                                estudiante["edad"] = edad_actualizada              # Actualizamos la edad del estudiante.
                                break                                              # Salimos del bucle de entrada de edad.
                            else:
                                print("Error: La edad debe estar en el rango de 15 a 90 años.")  #Mensaje de error fuera de rango.
                        else:
                            print("Error: La edad debe ser un número entero válido.")  #Mensaje de error si no es un número.

                    # Nuevo promedio
                    while True:  # Bucle para la entrada del nuevo promedio.
                        promedio_actualizado = input("Ingrese el nuevo promedio: ")  #Solicitamos al usuario que ingrese el nuevo promedio.
                        try:
                            promedio_actualizado = float(promedio_actualizado)      #Convertimos la entrada a flotante.
                            if 0.0 <= promedio_actualizado <= 5.0:                  #Verificamos si el promedio está en el rango válido.
                                estudiante["promedio"] = promedio_actualizado       #Actualizamos el promedio del estudiante.
                                print(f"Información de {cedula_estudiante} actualizada.")  #Mensaje de confirmación.
                                break                                               #Salimos del bucle de entrada de promedio.
                            else:
                                print("Error: El promedio debe estar entre 0.0 y 5.0.")  #Mensaje de error fuera de rango.
                        except ValueError:
                            print("Error: El promedio debe ser un número decimal válido.")  #Mensaje de error si no es un número decimal.
                    break                                                           #Salimos del bucle principal después de actualizar los datos.

                else:
                    print("Error: Selección de estudiante no válida.")              #Mensaje de error si la selección no es válida.
            except ValueError:
                print("Error: Ingrese un número válido como selección.")            #Mensaje de error si no se ingresa un número válido.
    else:
        print("No hay estudiantes registrados.")                                    #Mensaje si no hay estudiantes registrados.


#___________________________________________________________________________________________________________________________
def show_students():
    '''
    Mostrar todos los estudiantes en forma de tabla
    '''

    if len(estudiantes) > 0:                # Verifica si hay estudiantes en el diccionario 'estudiantes'.
        print("\nLista de Estudiantes:")    # Imprime un encabezado para la lista de estudiantes.
        
        # Encabezado de la tabla con formato
        print("{:<10} {:<10} {:<10} {:<10} {:<30}".format("Cédula","Nombre", "Edad", "Promedio", "Carrera"))  # Imprime un encabezado formateado.
        print("-" * 60)                     # Imprime una línea horizontal para separar el encabezado de los datos.

        for cedula, datos in estudiantes.items():   # Itera a través de los estudiantes y sus datos en el diccionario 'estudiantes'.
            nombre = datos["nombre"]                # Obtuene el nombre del estudiante.
            edad = datos["edad"]                    # Obtiene la edad del estudiante.
            carrera_numero = datos["carrera"]       # Obtiene el código de carrera del estudiante.
            promedio = datos["promedio"]            # Obtiene el promedio del estudiante.
            nombre_carrera = carreras[carrera_numero]  # Obtiene el nombre de la carrera correspondiente al código de carrera.
            
            # Imprime los datos del estudiante formateados en una fila de la tabla.
            print("{:<10} {:<10} {:<10} {:<10} {:<30}".format(cedula, nombre, edad, promedio, nombre_carrera))

    else:
        print("No hay estudiantes registrados.")    #Imprime un mensaje si no hay estudiantes en el diccionario 'estudiantes'.
         
#_____________________________________________________________________________________________________________________

def delete_student():
    '''
    Eliminar un estudiante del registro
    '''
    if len(estudiantes) > 0:            # Verifica si hay estudiantes.
        
        print("Lista de Estudiantes:")  # Mostrar la lista de estudiantes con un número de identificación
        i = 1                           # Inicializamos un contador para numerar a los estudiantes
        for cedula, datos in estudiantes.items():  # Iteramos sobre el diccionario de estudiantes
            print(f"{i}. Cédula: {cedula}, Nombre: {datos['nombre']}, Edad: {datos['edad']}, Carrera: {datos['carrera']}, Promedio: {datos['promedio']}")
            i += 1  # Incrementamos el contador

        while True:
            try:
                seleccion = int(input("Ingrese el número del estudiante a eliminar: "))

                if 1 <= seleccion <= len(estudiantes):                           # Verificamos que la selección sea válida
                    cedula_estudiante = list(estudiantes.keys())[seleccion - 1]  # Obtenemos la cédula del estudiante a eliminar
                    del estudiantes[cedula_estudiante]                           # Elimina al estudiante del diccionario
                    print(f"Estudiante {cedula_estudiante} eliminado del registro.")
                    break

                else:
                    print("Error: Selección de estudiante no válida.")
            except ValueError:
                print("Error: Ingrese un número válido como selección.")
    else:
        print("No hay estudiantes registrados.")                         # Si no hay estudiantes en el registro, muestra un mensaje.


#_____________________________________________________________________________________________________________________

def menu():
    try:
        while True:
            print("\nMenu:")
            print("1. Registrar estudiante")
            print("2. Consultar estudiantes de una carrera")
            print("3. Calcular promedio general")
            print("4. Ver estudiantes destacados de toda la universidad")
            print("5. Ver estudiantes destacados por carrera")
            print("6. Actualizar información del estudiante")
            print("7. Base de datos de estudiantes")
            print("8. Eliminar estudiantes")
            print("9. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                register()
            elif opcion == "2":
                students_inquiry()
            elif opcion == "3":
                general_average()
            elif opcion == "4":
                best_students()
            elif opcion == "5":
                best_students_by_career()
            elif opcion == "6":
                update_students()
            elif opcion == "7":
                show_students()
            elif opcion == "8":
                delete_student()
            elif opcion == "9":
                save_data()
                print("Saliendo del programa. La base de datos ha sido guardada.")
                break                                           #Salir del bucle si cumple la condición.
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    except KeyboardInterrupt:                               # Si se le da stop a la consola.
        save_data()
        print("""\n
              Adiós.
              la base de datos fue guardada en caso de haber completado totalmente el registro
              Ocurrió interrupción del usuario.""")

#_____________________________________________________________________________________________________________________
