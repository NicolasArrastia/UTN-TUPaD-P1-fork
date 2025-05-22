# --- 1 --- #
def factorial(num):
    if num<=1:
        return num
    else:
        return num * factorial(num-1)

# print(factorial(5)) # 120

# --- 2 --- #
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1)+fibonacci(pos-2)

# limite = int(input("Ingrese la posicion de fibonacci: "))
# for i in range(limite+1):
#     print(fibonacci(i), end=f"{", " if i != limite else "\n"}")

# --- 3 --- #
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))
# print(f"resultado = {potencia(base,exponente)}")

# --- 4 --- #
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n%2)

# numero = int(input("Ingrese un numero entero positivo: ")) # 255 = 11111111
# if numero == 0:
#     print("0")
# else:
#     print(decimal_a_binario(numero))

# --- 5 --- #
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# texto = input("Ingrese una palabra: ") # reconocer = True, palindromo = False
# print(es_palindromo(texto))

# --- 6 --- #
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# numero = int(input("Ingrese un número entero positivo: "))
# print(suma_digitos(numero))

# --- 7 --- #
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# nivel_inferior = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
# print(contar_bloques(nivel_inferior))


# --- 8 --- #
def contar_digito(numero,digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)
# print(contar_digito(12233421, 2)) # 3
