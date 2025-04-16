# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(1,101,1): # Ciclo for que va desde el 1 hasta el 100 incrementando por 1
#     print(i) # imprime i

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# num = input("Ingrese un número: ")
# print(f"Su número tiene {len(num)} digitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese un número.\n")) # Pedimos un número
# num2 = int(input("Ingrese otro número.\n")) # Pedimos otro número

# num1 = num1 +1 # Le sumamos 1 a num1 para excluir ese valor
# suma = 0 # Inicializamos suma en 0

# for i in range(num1,num2): # Bucle for que va desde num1+1 hasta num2 
#     suma = suma + i # Vamos sumando cada dígito obtenido del bucle
# print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# num = int(input("Ingrese un número. "))
# suma = 0

# while num != 0:
#     suma = suma + num
#     num = int(input("Ingrese un número. "))

# print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random

# num = random.randint(0,9)
# numUser = int(input("Adivina el número entre 0 y 9.\n"))
# contador = 1
# while num != numUser:
#     numUser = int(input("Adivina el número entre 0 y 9.\n"))
#     contador += 1
# print(f"El número era {num} y te tomo {contador} intentos, felicitaciones!!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(2,101,2):
#     print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# numUser = int(input("Ingrese un número entero positivo.\n"))
# numUser +=1
# suma = 0
# for i in range(0,numUser):
#     suma = suma + i
# print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# cont = 0
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# while cont < 100:
#     numUser = int(input("Ingrese un número.\n"))
#     if numUser % 2 == 0:
#         pares +=1
#     if numUser % 2 == 1:
#         impares +=1
#     if numUser > 0:
#         positivos +=1
#     if numUser < 0:
#         negativos +=1
#     cont +=1
# print(f"Ingresaste {cont} números, de los cuales {pares} fueron pares, {impares} fueron impares, {positivos} fueron positivos y {negativos} fueron negativos.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# from statistics import mean
# media = []
# cant = 0
# while cant < 100 :
#     num = int(input("Ingrese un número.\n"))
#     media.append(num)
#     cant +=1
# resultado = mean(media)
# print(f"La media de los valores ingresados es {resultado}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# numUser = input("Ingrese un número.\n")
# invertido = ""
# for i in range(-1,-len(numUser)-1,-1):
#     invertido = invertido + numUser[i]
# print(invertido)