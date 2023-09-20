import os
import datetime
import platform

def mostrar_ayuda():
    print("Comandos permitidos:")
    print("pwd - Muestra el directorio activo.")
    print("date - Muestra la fecha actual.")
    print("time - Muestra la hora actual.")
    print("exit - Sale del intérprete o programa.")
    print("clear - Borra la pantalla.")
    print("man - Proporciona ayuda de los comandos.")
    print("uname -a - Muestra la versión del OS.")
    print("cd [directorio] - Cambia el directorio activo.")
    print("ls [opciones][dir] - Muestra el contenido del directorio especificado.")
    print("rm [archivos] - Borra archivos.")
    print("mkdir [directorio] - Crea un directorio.")
    print("rmdir [directorio] - Borra un directorio.")

def version_os():
    system_info = platform.uname()
    for key, value in zip(system_info._fields, system_info):
        print(f"{key}: {value}")

def cambiardirectorio(directorio):
    try:
        os.chdir(directorio)
    except FileNotFoundError:
        print(f"Directorio no encontrado: {directorio}")

def listardirectorio(opciones=""):
    try:
        with os.scandir() as archivos:
            for archivo in archivos:
                if opciones != "-a" and archivo.name.startswith("."):
                    continue
                if opciones == "-l":
                    print(f"{archivo.name} {archivo.stat()}")
                else:
                    print(archivo.name)
    except FileNotFoundError:
        print(f"Directorio no encontrado: {os.getcwd()}")

def borrararchivo(*archivos):
    for archivo in archivos:
        try:
            os.remove(archivo)
            print(f"Archivo borrado: {archivo}")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        except PermissionError:
            print(f"No tienes permisos para borrar: {archivo}")

def creardirectorio(directorio):
    try:
        os.mkdir(directorio)
        print(f"Directorio creado: {directorio}")
    except FileExistsError:
        print(f"El directorio ya existe: {directorio}")

def borrardirectorio(directorio):
    try:
        os.rmdir(directorio)
        print(f"Directorio borrado: {directorio}")
    except FileNotFoundError:
        print(f"Directorio no encontrado: {directorio}")
    except OSError:
        print(f"No se puede borrar el directorio: {directorio}")