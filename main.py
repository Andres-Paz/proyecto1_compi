from funciones import *

comandos = {
    "pwd": lambda: print(os.getcwd()),
    "date": lambda: print(datetime.date.today()),
    "time": lambda: print(datetime.datetime.now().time()),
    "exit": exit,
    "clear": lambda: os.system('cls' if os.name == 'nt' else 'clear'),
    "man": mostrar_ayuda,
    "uname -a": version_os,
    "cd": cambiardirectorio,
    "ls": listardirectorio,
    "rm": borrararchivo,
    "mkdir": creardirectorio,
    "rmdir": borrardirectorio,
}

while True:
    comando = input("> ")
    partes = comando.split(" ", 1)
    if partes[0] in comandos:
        comandos[partes[0]](*partes[1:])
    else:
        print("Comando no reconocido")
