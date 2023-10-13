'''
Programa principal
Registro y Consulta de estudiantes Universitarios 

Sebastián Alzate Sierra
Maria Paula Ramos
xxxxxxxxxxxxxxxx

Taller #2 Programación
'''
import functions as ft

def run():
    ft.load_data()  # Cargar base de datos si existe
    ft.menu()       # Ejecutar el menú

#Entry Point
if __name__ == "__main__": # Determina si el archivo actual se está ejecutando como programa principal.
    print("\nCÓDIGO PRINCIPAL\n ") # Imprimir un mensaje indicando que se está ejecutando el código principal.
    run()  # Llamar a la función 'run' para iniciar la ejecución del programa.
    
