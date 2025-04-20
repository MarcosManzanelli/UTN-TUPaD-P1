# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}, es un placer!")

# nombre = input("Hola, ¿Cómo te llamas?\n")
# saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

# nombre = input("¿Cuál es tu nombre?\n")
# apellido = input("¿Cuál es tu apellido?\n")
# edad = input("¿Cuál es tu edad?\n")
# residencia = input("¿Cuál es tu lugar de residencia?\n")

# informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.

# import math

# def calcular_area_circulo(radio):
#     return math.pi * (radio*radio)

# def calcular_perimetro_circulo(radio):
#     return math.pi * (radio*2)

# radio = int(input("Ingrese el radio de un circulo.\n"))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El area de su circulo es {round(area,2)} y el perimetro es {round(perimetro,2)}.")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     minutos = 0
#     hora = 0
#     while segundos >= 60:
#         minutos +=1
#         if minutos >= 60:
#             hora +=1
#             minutos=0
#         segundos = segundos - 60
#     return f"{hora}:{minutos}:{segundos}"

# segundos = int(input("Ingrese segundos.\n"))
# hora = segundos_a_horas(segundos)
# print(f"La hora es {hora}")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.

# def tabla_multiplicar(numero):
#     print(f"{numero} X 1 = {1*(numero)}")
#     print(f"{numero} X 2 = {2*(numero)}")
#     print(f"{numero} X 3 = {3*(numero)}")
#     print(f"{numero} X 4 = {4*(numero)}")
#     print(f"{numero} X 5 = {5*(numero)}")
#     print(f"{numero} X 6 = {6*(numero)}")
#     print(f"{numero} X 7 = {7*(numero)}")
#     print(f"{numero} X 8 = {8*(numero)}")
#     print(f"{numero} X 9 = {9*(numero)}")
#     print(f"{numero} X 10 = {10*(numero)}")

# numero = int(input("Ingrese un número para saber la tabla de multiplicar del mismo.\n"))
# tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     mult = a * b
#     div = a // b
#     return print(f"La suma de {a} y {b} es {suma}\nLa resta de {a} y {b} es {resta}\nLa multiplicaión de {a} y {b} es {mult}\nLa división de {a} y {b} es {div}")

# num1 = int(input("Ingrese el primer número.\n"))
# num2 = int(input("Ingrese el segundo número.\n"))
# operaciones_basicas(num1,num2)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#     return peso / (altura*altura)

# peso = float(input("Ingrese su peso.\n"))
# altura = float(input("Ingrese su altura.\n"))
# imc = calcular_imc(peso, altura)
# print(f"Su IMC es {round(imc,2)}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
# celsius = float(input("Indique la tempertura en grados celsius.\n"))
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"La temperatura {round(celsius,2)} grados en celsius equivalen a {round(fahrenheit,2)} grados en fahrenheit.")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

# def calcular_promedio(a,b,c):
#     return (a+b+c) / 3

# nota1 = int(input("Indique la primer nota.\n"))
# nota2 = int(input("Indique la segunda nota.\n"))
# nota3 = int(input("Indique la tercer nota.\n"))
# promedio = calcular_promedio(nota1,nota2,nota3)
# print(f"Su promedio final es {round(promedio,2)}")