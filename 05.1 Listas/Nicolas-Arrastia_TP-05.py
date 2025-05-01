# Actividad 1
my_list = list(range(4,101,4))
print(my_list)

# Actividad 2
five_items = [3.14, 42, 1.618, 'Linus', 'Torvald']
print(five_items[-2])

# Actividad 3
mty_list = []
mty_list.append("uno")
mty_list.append("dos")
mty_list.append("tres")
print(mty_list)

# Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[-2] = "loro"
animales[-1] = "oso"
print(animales)

# Actividad 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
"""
1. Define la varible "numeros" con una lista que incluye los numeros: 8, 15, 3, 22, 7
2. Busca el valor máximo con la función `max` y procede a removerla del arreglo con `remove`
3. Imprime por pantalla la lista modificada de numeros
"""

# Actividad 6
ten_to_thirty = list(range(10,31,5))
print(ten_to_thirty)

# Actividad 7
autos = ["sedan","polo","suran","gol"]
print(autos)
autos[1] = "cuales"
autos[2] = "quiera"
print(autos)

# Actividad 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugos")

fideos_index = compras[1].index("fideos")
compras[1][fideos_index] = "tallarines"
# Tambien se puede hacer de la siguiente forma
# compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

# Actividad 10
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)

