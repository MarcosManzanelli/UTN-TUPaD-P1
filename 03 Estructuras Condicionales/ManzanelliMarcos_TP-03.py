# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad. "))
# mayorDeEdad = 18

# if edad >= mayorDeEdad:
#     print("Es mayor de edad.")
# else:
#     pass

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int(input("Ingrese su nota. "))

# if nota >= 6:
#     print("Aprobado.")
# else:
#     print("Desaprobado.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# num = int(input("Ingese un número par. "))

# if num % 2 == 0:
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad. "))

# if edad < 12:
#     print("Es un niño/a.")
# elif edad >= 12 and edad < 18:
#     print("Es un adolecente.")
# elif edad >= 18 and edad < 30:
#     print("Es un adulto/a joven.")
# elif edad >= 30:
#     print("Es un adulto/a.")
# else:
#     pass

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# pwd = len(input("Ingrese una contraseña entre 8 y 14 carácteres. "))

# if pwd >= 8 and pwd <= 14:
#     print("Ha ingresado una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 carácteres.")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# from statistics import mode, median, mean
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)


# if media > mediana and mediana > moda:
#     print("Sesgo positivo o a la derecha.")
# elif moda > mediana and mediana < moda:
#     print("Sesgo negativo o a la izquierda.")
# elif media == mediana and mediana == moda:
#     print("Sin sesgo.")
# else:
#     pass

# print(f"Lista generada: {numeros_aleatorios}")
# print(f"Moda: {moda}, Mediana: {mediana}, Media: {media:.2f}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

