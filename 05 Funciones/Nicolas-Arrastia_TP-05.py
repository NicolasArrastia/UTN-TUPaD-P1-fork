def print_title(number):
    print("- - - - - - - - - - - - - - - - - - - ")
    print(f"Ejericio {number}\)")
# -----
# - 1 -
# -----
print_title(1)
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# -----
# - 2 -
# -----
print_title(2)
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre_usuario = input("Ingrese nombre: ")
saludar_usuario(nombre_usuario)

# -----
# - 3 -
# -----
print_title(3)
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

# -----
# - 4 -
# -----
print_title(4)
def calcular_area_circulo(radio):
    return 3.14*radio**2
def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

radio = float(input("Ingrese el radio del circulo: "))

print(f"Area: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")

# -----
# - 5 -
# -----
print_title(5)
def segundos_a_horas(segundos):
    return segundos/60/60
segundos=int(input("Ingrese los segundos: "))
print(f"Segundos en horas: {segundos_a_horas(segundos)}")

# -----
# - 6 -
# -----
print_title(6)
def tabla_multiplicar(numero):
    for i in range(10):
        print((i+1)*numero)
numero=int(input("Ingrese numero para imprimir la tabla de multiplicar: "))
tabla_multiplicar(numero)

# -----
# - 7 -
# -----
print_title(7)
def operaciones_basicas(a,b):
    print(f"Suma: {a+b}")
    print(f"Resta: {a-b}")
    print(f"Multiplicacion: {a*b}")
    if b != 0:
        print(f"Division: {a/b}")
    else:
        print("No se puede dividir por cero ({b})")

numero_a = float(input("Ingrese numero a: "))
numero_b = float(input("Ingrese numero b: "))
operaciones_basicas(numero_a, numero_b)

# -----
# - 8 -
# -----
print_title(8)
def calcular_imc(peso, altura):
    return peso/(altura**2)
peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))
print(f"Su IMC = {calcular_imc(peso,altura)}")

# -----
# - 9 -
# -----
print_title(9)
def celsius_a_fahrenheit(celsius):
    return (celsius*1.8)+32

celsius = float(input("Ingrese grados Celsius: "))
print(f"F = {celsius_a_fahrenheit(celsius)}")

# ------
# - 10 -
# ------
print_title(10)
def calcualr_promedio(a,b,c):
    return (a+b+c)/3
nota_a = float(input("Ingrese nota a: "))
nota_b = float(input("Ingrese nota b: "))
nota_c = float(input("Ingrese nota c: "))
print(f"Su promedio es: {calcualr_promedio(nota_a,nota_b,nota_c)}")

