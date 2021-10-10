import math
import numpy as np
print("Primer ejerecicio")
#Primer ejercicio:  El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
ket = [] #inicializo el ket como un arreglo
ket = input("Digite los componenetes del ket como numeros complejos de python(separados por un espacio): ") #los componenetes del ket deben ser numeros complejos como los recibe python, por ejemplo: -3-j -2j j 2
ket = ket.split(" ")
print(f"el ket tiene {len(ket)} estados") #Se indica cuantos estados tiene el ket segun el numero de componentes

for i in range(len(ket)): #Con este ciclo combierto los elementos del ket en numeros complejos
    ket[i] = complex(ket[i])
print(f"El ket introducido es: {ket}")

for i in range(len(ket)): #Con este ciclo saco la suma de los cuadrados de la parte real y la imaginaria de cada componente del ket
    Z = ket[i]
    a = Z.real
    b = Z.imag
    t = (a**2 + b**2)
    ket[i] = t
suma = 0
for i in range(len(ket)): #Con este ciclo saco la longitud del ket
    suma = suma + int(ket[i])
    result = math.sqrt(suma)
print(f"La longitud del ket es: {result}")
estado = int(input("Digite la posicion que desea(digitelo como un numero entero): ")) #Pregunto en que estado se quiere ver la probabilidad
probabilidad = ket[estado]**2/result**2  #Saco la probabilidad de que la canica este en el estado.
print(f"La probabilidad de que la particula este en la posicion {estado} es {probabilidad}%") #Devuelvo la probabilidad deque la canica este en el estado. 


print("Segundo Ejericico")
#Segundo Ejercicio: El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
ket = [] #inicializo el ket como un arreglo
ket = input("Digite los componenetes del ket como numeros complejos de python(separados por un espacio): ") #los componenetes del ket deben ser numeros complejos como los recibe python, por ejemplo: -3-j -2j j 2
ket1 = ket #creo otro ket igual al ket original
ket2 = ket #creo otro ket igual al ket original
ket1 = ket1.split(" ") #
ket2 = ket2.split(" ") #
ket = ket.split(" ") #

for i in range(len(ket1)): #Con este ciclo combierto los elementos del ket1 en numeros complejos
    ket1[i] = complex(ket1[i])

for i in range(len(ket)): #Con este ciclo combierto los elementos del ket en numeros complejos
    ket[i] = complex(ket[i])

for i in range(len(ket2)): #Con este ciclo combierto los elementos del ket2 en numeros complejos
    ket2[i] = complex(ket2[i])

print(f"El ket introducido es: {ket1}")

for i in range(len(ket1)): #Con este ciclo saco la suma de los cuadrados de la parte real y la imaginaria de cada componente del ket1
    Z = ket1[i]
    a = Z.real
    b = Z.imag
    t = (a**2 + b**2)
    ket1[i] = t

suma = 0
for i in range(len(ket1)): #Con este ciclo saco la longitud del ket1
    suma = suma + int(ket1[i]) 
    result = math.sqrt(suma)

for i in range(len(ket)): #Con este ciclo normalizo el ket original
    Z = ket[i]
    a = Z.real/result
    b = Z.imag/result
    ket[i] = (a, b)

print(f"El ket normalizado es: {ket}")

for i in range(len(ket2)): #Con este ciclo normalizo el bra del ket original
    Z = ket2[i]
    a = Z.real/result
    b = Z.imag/result
    ket2[i] = (a, b*-1)

print(f"El bra normalizado es: {ket2}")
print(f"La amplitud de transicion seria {ket} * {ket2}")