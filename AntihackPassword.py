import random
from unicodedata import name

print("***************************************************")
print("\nBienvenido al generador de contraseñas Antihackeos")
print("\n***************************************************")

nombre = input("Cual es tu nombre: ")

print("Bienvenido " + nombre + " es un placer tenerte por aqui")
print("***************************************************")

rango = int(input("Cuantas contraseñas necesitas en esta ocasion: "))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbols = "*+!#$%&"
numbers = "1234567890"

na = input("nombre del archivo donde se guardaran las contraseñas: ")
name = na + ".txt"

len = int(input("Que tan larga es la contraseña que necesitas: "))

sum = lower + upper + simbols + numbers

archivo = open(name, "w")
archivo.write("Bienvenido " + nombre + " Aqui se guardaran tus contraseñas")

for i in range(rango):
        uso = input("Para que necesitas de esta contraseña: ")
        password = "".join(random.sample(sum, len))
        print("Tu contraseña Antihackeos de esta ocasion es: --> | " + password + " | <-- para: " + uso)
        archivo.write("\n****************************************************************************************")
        archivo.write("\n\tTu contraseña Antihackeos de esta ocasion es: --> | " + password + " | <-- para: " + uso)
        archivo.write("\n*---------------------------------------------------------------------------------------*")

archivo.write("\nA modo de recomendacion de seguridad procure cambiar la contraseña de su servicio con minimo un mes de antiguedad")
archivo.write("\n\tTenga un excelente dia")
archivo.close()