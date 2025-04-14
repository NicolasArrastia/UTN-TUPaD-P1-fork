# 1
# edad = int(input("Ingrese su edad:"))
# if edad >= 18:
#     print("Es mayor de edad")

# 2
# nota = float(input("Ingrese su nota:"))
# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# 3
# numero_par = int(input("Ingrese un numero par:"))
# if numero_par % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# 4
# edad = int(input("Ingrese su edad:"))
# if edad < 12:
#     print("Niño/a")
# elif edad < 18:
#     print("Adolescente")
# elif edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")

# 5
# password = input("Ingrese una contraseña")
# if 8 <= len(password) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña correcta")

# 6
# from statistics import mode, median, mean
# import random
#
# random_numbers = [random.randint(1,100) for i in range(50)]
#
# moda = mode(random_numbers)
# mediana = median(random_numbers)
# media = mean(random_numbers)
#
# if media > mediana and mediana > moda:
#     print("Sesgo positivo o a la derecha")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo o a la izquierda")
# elif media == mediana == moda:
#     print("Sin sesgo")
# else:
#     print("No hay sesgo definido")

# 7
# frase = input("Ingrese una frase: ")
# ultima_letra = frase[-1].lower()
#
# if ultima_letra in "aeiou":
#     print(f"{frase}!")
# else:
#     print(frase)

# 8
# nombre = input("Ingrese su nombre: ")
# print("Ingrese la opción que desee:")
# print("1. MAYÚSCULAS")
# print("2. minusculas")
# print("3. Primera letra en mayúscula")
# opcion = int(input())
#
# if opcion == 1:
#     print(f"{nombre.upper()}")
# elif opcion == 2:
#     print(f"{nombre.lower()}")
# elif opcion == 3:
#     print(f"{nombre.title()}")
# else:
#     print("Opción no valida")

# 9
# magnitud = float(input("Ingrese la magnitud del terremoto: "))
#
# if magnitud < 3:
#     print("Muy leve")
# if 3 <= magnitud < 4:
#     print("Leve")
# if 4 <= magnitud < 5:
#     print("Moderado")
# if 5 <= magnitud < 6:
#     print("Fuerte")
# if 6 <= magnitud < 7:
#     print("Muy Fuerte")
# if magnitud >= 7:
#     print("Extremo")

# 10
# hemisferio = input("Ingrese el hemisferio (N/S): ").lower()
# mes = int(input("Ingrese el número de mes (1-12): "))
# dia = int(input("Ingrese el día del mes: "))
#
# if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#     estacion_n = "Invierno"
#     estacion_s = "Verano"
# elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#     estacion_n = "Primavera"
#     estacion_s = "Otoño"
# elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#     estacion_n = "Verano"
#     estacion_s = "Invierno"
# else:
#     estacion_n = "Otoño"
#     estacion_s = "Primavera"
#
# if hemisferio == "n":
#     print(f"Estás en {estacion_n}")
# elif hemisferio == "s":
#     print(f"Estás en {estacion_s}")
# else:
#     print("Hemisferio no válido")
