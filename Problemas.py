import math
import numpy as np

#REALICE LOS SIGUIENTES PROBLEMAS E INCLUYALOS COMO EJEMPLOS

#4.4.1
print("En este ejercicio tenemos que verificar que dos matrices sean unitarias y que su podructo tambien sea unitario")
matriz1 = []
for i in range(2):
    matriz1.append([0]*2)
matriz1[0][1] = 1 
matriz1[1][0] = 1 
matriz2 = []
for i in range(2):
    matriz2.append([0]*2)
matriz2[0][0] = "√2/2"
matriz2[0][1] = "√2/2"
matriz2[1][0] = "√2/2"
matriz2[1][1] = "-√2/2"
matriz3 = []
for i in range(2):
    matriz3.append([0]*2)
matriz3[0][0] = 1 
matriz3[1][1] = 1 
matriz4 = []
for i in range(2):
    matriz4.append([0]*2)
matriz4[0][0] = "√2/2"
matriz4[0][1] = "-√2/2"
matriz4[1][0] = "√2/2"
matriz4[1][1] = "√2/2"
matriz5 = []
for i in range(2):
    matriz5.append([0]*2)
matriz5[0][0] = "√2/2"
matriz5[0][1] = "√2/2"
matriz5[1][0] = "-√2/2"
matriz5[1][1] = "√2/2"

print("Miramos si u1 es unitaria")
print(f"La matriz u1 = {matriz1} y su adjunta es u1t= {matriz1}")
print(f"Para saber si u1 es unitaria multiplicamos u1t por u1")
print(f"{matriz1}*{matriz1} = {matriz3}")
print("Podemos ver que u1 es UNITARIA")
print("Ahora miramos si u2 es unitaria")
print(f"La matriz u2 = {matriz2} y su adjunta es u2t= {matriz2}")
print(f"Para saber si u2 es unitaria multiplicamos u2t por u2")
print(f"{matriz2}*{matriz2} = {matriz3}")
print("Podemos ver que u2 es UNITARIA")
print("Ahora tenemos que mirar si el resultado de la multiplicacion entre u1 y u2 es unitaria")
print(f"u3 = {matriz1}*{matriz2}")
print(f"{matriz4} = {matriz1}*{matriz2}")
print("Ahora miramos si u3 es unitaria")
print(f"Para saber si u3 es unitaria multiplicamos u3t por u3")
print(f"{matriz5}*{matriz4} = {matriz3}")
print("Podemos ver que u3 es UNITARIA")
print("Con esto podemos teminar el ejercicio 4.4.1")

#4.4.2
print("En este ejericico debemos determinar el estado del sistema despues de tres clicks y mirar la probabilidad de que la canica se encuentre en el punto 3")

print("U es igual a")
matriz = []
for i in range(4):
    matriz.append([0]*4)
matriz[0][1] = "1/√2"
matriz[0][2] = "1/√2"
matriz[1][0] = "i/√2"
matriz[1][3] = "1/√2"
matriz[2][0] = "1/√2"
matriz[2][3] = "i/√2"
matriz[3][1] = "1/√2"
matriz[3][2] = "-1/√2"
matriz = np.array(matriz)

print(matriz)
print("Como en el sistema tenemos entradas con i, le sacamos el modulo al cuadrado a la matriz")
print("El modulo al cuadrado de la matriz (|U|^2) es")

matriz2 = []
for i in range(4):
    matriz2.append([0]*4)
matriz2[0][1] = "1/2"
matriz2[0][2] = "1/2"
matriz2[1][0] = "1/2"
matriz2[1][3] = "1/2"
matriz2[2][0] = "1/2"
matriz2[2][3] = "1/2"
matriz2[3][1] = "1/2"
matriz2[3][2] = "1/2"
matriz2 = np.array(matriz2)
print(matriz2)
matriz3 = []
for i in range(4):
    matriz3.append([0]*1)
matriz3[0][0] = "1"
matriz3[1][0] = "0"
matriz3[2][0] = "0"
matriz3[3][0] = "0"

matriz2 = np.array(matriz2)
print("Como necesitamos el estado del sistema despues de 3 clicks, podemos elevar U al cubo y multiplicarlo por el estado inicial")
print("U^3 es")
print(matriz2)
print("Vector estado inicial es")
matriz3 = np.array(matriz3)
print(matriz3)
print("Al multiplicar estos dos, nos da como resultado el vector")
matriz4 = []
for i in range(4):
    matriz4.append([0]*1)
matriz4[0][0] = "0"
matriz4[1][0] = "1/2"
matriz4[2][0] = "1/2"
matriz4[3][0] = "0"
matriz4 = np.array(matriz4)
print(matriz4)
print("La probabilidad de que la bola cuantica se encuentre en el punto 3 es de 0%")
print("Con esto podemos teminar el ejercicio 4.4.2")