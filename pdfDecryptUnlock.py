"""
Finalidad del programa: Este programa tiene por cometido desbloquear(quitar la contraseña) un fichero pdf de nuestra elección, cuya contraseña evidentemente no conocemos
Tras acertar por medio de fuerza bruta con la contraseña, copiamos el contenido del pdf original a uno nuevo sin contraseña, además la contraseña queda en la terminal escrita
Autor: Francisco Javier Pizarro
Última revisión:14/04/2021
Comentarios: El coste computacional del programa aumenta de manera EXPONENCIAL según aumenta el rango de la contraseña, esto causa que cuanto más larga sea la posible contraseña 
más absurdamente largo será el tiempo de ejecución del programas
"""
#importamos los módulos necesarios
import pikepdf
from itertools import product
import string
from termcolor import colored
#guardamos la ruta del pdf original y generamos la nueva ruta para el pdf desbloqueado
print("El fichero pdf puede ser referenciado relativamente(si se encuentra en la misma carpeta que el programa) introduciendo solo el nombre")
print("En caso contrario debe introducir la ruta COMPLETA desde el disco en el que se encuentre")
ruta = input("Introduzca el nombre del archivo pdf(sin la extensión)\n")
ruta = ruta + ".pdf"
ruta2 = "Unlocked" + ruta
#generamos una lista de carácteres para la fuerza bruta
contraseñas = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
contraseñas.append("")
#definimos la máxima longitud de la contraseña
Rmax = int(input("Introduzca la máxima longitud de la clave\n")) + 1
#booleano auxiliar para parar el bucle
encontrado = False
#iteramos dentro del rango de la contraseña
for i in range(0, Rmax):
    if not encontrado:
        #probamos para el rango en el que nos encontremos todas las posibles permutaciones de los elementos de la lista de carácteres
        for pwd in product(contraseñas,repeat=i):
            #cambiamos el formato de la contraseña de lista a string
            passwd = "".join(pwd)
            #probamos la contraseña
            try:
                with pikepdf.open(ruta,passwd) as pdf:
                    #si funciona clonamos el contenido del pdf original a otro sin contraseña
                    print(colored("Contraseña encontrada:" + passwd,"green"))
                    pdf.save(ruta2)
                    encontrado = True
                    break
            #en caso de que falle
            except:
                print(colored("Intentando contraseña:" + passwd,"red"))
                continue