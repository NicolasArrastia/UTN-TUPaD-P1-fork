# 1
# for i in range(101):
#     print(i)

# 2
# numero = int(input("Ingrese un numero entero"))
# contador = 0
# for i in str(abs(numero)):
#     contador += 1
# print(contador)

# 3
# min_number = int(input("Ingrese el numero minimo: "))
# max_number = int(input("Ingrese el numero maximo: "))
# total_sum = 0
# for i in range(min_number, max_number+1, 1):
#     total_sum = total_sum + i
# print(f"Total: {total_sum}")

# 4
# total=0
# add_number=-1
# print("Ingrese un numero para agregarlo a la suma (Ingrese 0 para finalizar)")
# while add_number != 0:
#     print(f"Total actual: {total}")
#     add_number = int(input())
#     total=total+add_number
# print(f"Total sumado: {total}")

# 5
# from random import randint
# random_number=randint(0,9)
# attempts=1
# guessed_number=-1
# while guessed_number != random_number:
#     guessed_number = int(input("Adivina el número"))
#     if guessed_number != random_number:
#         attempts+=1
# print(f"Ha adivinado. Intentos totales: {attempts}")

# 6
# for i in range(100,0,-2):
#     print(i)

# 7
# input_number = int(input("Ingrese un numero entero positivo: "))
# total=0
# for i in range(0,input_number+1):
#     total+=i
# print(f"La suma total de todos los numeros desde 0 hasta {input_number} es: {total}")

# 8
# positive_total=0
# negative_total=0
# odd_total=0
# even_total=0
# zero_total=0
# for i in range(100):
#     input_number=int(input("Ingrese un numero entero: "))
#     if input_number % 2 == 0:
#         even_total+=1
#     elif input_number % 2 != 0:
#         odd_total+=1
#     if input_number > 0:
#         positive_total+=1
#     elif input_number < 0:
#         negative_total+=1
#     if input_number == 0:
#         zero_total+=1
# print(f"Positivos: {positive_total}")
# print(f"Negativos: {negative_total}")
# print(f"Pares: {even_total}")
# print(f"Impares: {odd_total}")
# print(f"Ceros: {zero_total}")

# 9
# CANTIDAD = 100
# suma = 0
# for _ in range(CANTIDAD):
#     num = int(input("Ingresa un número entero: "))
#     suma += num
# media = suma / CANTIDAD
# print(f"La media es: {media}")

# 10
# numero = input("Ingrese un numero: ")
# output_numero = ""
# for i in range(len(numero),0,-1):
#     output_numero+=numero[i-1]
# print(output_numero)

