import os

def create_files():
    print("\nCreando 4 archivos y 2 carpetas...")
    os.system("mkdir D1 D2")
    print("Creando archivos a D1 y D2...")
    os.system("echo 'Primer Archivo' > D1/A")
    os.system("echo 'Segundo Archivo' > D1/B")
    os.system("echo 'Tercer Archivo' > D2/X")
    os.system("echo 'Cuarto Archivo' > D2/Y")
    print("Archivos creados y copiados exitosamente!")

def find_largest_file():
    print("\nBuscando el archivo mas grande en D1...")
    print("Archivo mas grande:")
    os.system("ls -S D1/ | head -n 1")

def compare_files():
    print("\nComparando archivos de D2...")
    print("Archivo mas actual:")
    os.system("ls -t D2/ | head -n 1")
    print("Archivo mas antiguo:")
    os.system("ls -tr D2/ | head -n 1")

def copy_contents():
    print("\nCopiando contenido de A en B...")
    os.system("cat D1/A >> D1/B")
    print("Contenido copiado exitosamente!")

def count_occurrences():
    print("\nContando ocurrencias de 'R' o 'r' en un archivo de D1...")
    print("Ocurrencias de 'R' y 'r' en el archivo A:")
    os.system("grep -o -i 'r' D1/A | wc -l")
    
def change_permissions():
    print("\nCambiando permisos de X a solamente ejecutable...")
    os.system("chmod 111 D2/X")
    print("Permisos cambiados exitosamente!")
    print("Comprobando permisos...")
    os.system("ls -l D2/X")

def change_owner():
    print("\nCambiando propietario de un archivo en D2...")
    os.system("sudo chown root D2/X")
    print("Propietario cambiado exitosamente!")
    print("Comprobando propietario...")
    os.system("ls -l D2/X")

def change_group():
    print("\nCambiando grupo del archivo Y...")
    os.system("sudo chgrp root D2/Y")
    print("Grupo cambiado exitosamente!")
    print("Comprobando grupo...")
    os.system("ls -l D2/Y")

def create_script():
    print("\nCreando script para cambiar el nombre de un archivo en D2...")
    os.system("echo '#!/bin/bash' > script.sh")
    os.system("echo 'mv D2/Y D2/Z' >> script.sh")
    os.system("chmod +x script.sh")
    print("Script creado exitosamente!")
    print("Comprobando script...")
    os.system("cat script.sh")

def encrypt_decrypt():
    print("\nEncriptando y desencriptando un archivo con gpg...")
    os.system("gpg -c D1/A")
    os.system("gpg D1/A.gpg")
    print("Archivo encriptado y desencriptado exitosamente!")

def exit_program():
    print("\nSaliendo del programa...")
    exit()

def ctrl_c():
    print("\nSaliendo del programa...")
    exit()


def show_menu():
    print("\nMenu:")
    print("1. Crear 4 archivos y copiarlos a D1 y D2.")
    print("2. Encontrar el archivo mas grande en D1.")
    print("3. Comparar archivos en D2.")
    print("4. Copiar contenido de A en B.")
    print("5. Contar ocurrencias de 'R' o 'r' en un archivo de D1.")
    print("6. Cambiar permisos de X a solamente ejecutable.")
    print("7. Cambiar propietario de un archivo en D2.")
    print("8. Cambiar grupo del archivo Y.")
    print("9. Crear script para cambiar el nombre de un archivo en D2.")
    print("10. Encriptar y desencriptar un archivo con gpg.")
    print("11. Salir del programa.")
    print("Presiona Ctrl + C para salir del programa.")
    option = input("Ingresa una opcion: ")
    return option

def execute_menu(option):
    if option == "1":
        create_files()
    elif option == "2":
        find_largest_file()
    elif option == "3":
        compare_files()
    elif option == "4":
        copy_contents()
    elif option == "5":
        count_occurrences()
    elif option == "6":
        change_permissions()
    elif option == "7":
        change_owner()
    elif option == "8":
        change_group()
    elif option == "9":
        create_script()
    elif option == "10":
        encrypt_decrypt()
    elif option == "11":
        exit_program()
    else:
        print("\nOpcion no valida, intenta de nuevo.")
        print("Presiona Ctrl + C para salir del programa.")
        option = input("Ingresa una opcion: ")
        execute_menu(option)

def execute_program():
    while True:
        option = show_menu()
        execute_menu(option)
        if option == "11":
            break

execute_program()