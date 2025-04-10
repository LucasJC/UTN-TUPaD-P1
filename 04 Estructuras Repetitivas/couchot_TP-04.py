# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("1)")
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num = int(input("2) Ingresar un entero: "))
aux = float(num)
digitos = 0
if 0 == num: 
    digitos = 1
while aux >= 1:
    aux = aux / 10
    digitos += 1
print(f"{num} tiene {digitos} dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("3) Ingresar un entero: "))
num2 = int(input("Ingresar otro entero: "))
total = 0
for i in range(num1 + 1, num2):
    total += i
print(f"Suma de nums entre ({num1};{num2}) = {total}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("4) ")
finalizar = False
total = 0
while(not finalizar):
    num = int(input("Ingrese un entero. 0 para finalizar: "))
    if 0 == num:
        break
    total += num
print(f"Suma total = {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("5) Adivine el número de 0 a 9:")
import random
resultado = random.randint(0, 9)
intentos = 0
ingresado = -1
while(resultado != ingresado):
    ingresado = int(input("Ingrese un número: "))
    intentos += 1
print(f"Ganaste! El número era {resultado}. Intentos: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("6) ")
for i in range(101, 0, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
num = int(input("7) Ingresar un entero: "))
total = 0
for i in range(0, num):
    total += i
print(f"Suma de nums entre (0;{num}) = {total}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("8)")
cantidad = 10
pares = 0
negativos = 0
for i in range(cantidad):
    num = int(input(f"Ingresar num {i+1} de {cantidad}: "))
    if num % 2 == 0:
        pares += 1
    if num < 0:
        negativos += 1
print(f"Pares: {pares}; Impares: {cantidad - pares}; Positivos: {cantidad - negativos}; Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("9)")
import statistics
cantidad = 10
nums = [None] * cantidad
for i in range(cantidad):
    nums[i] = int(input(f"Ingresar num {i+1} de {cantidad}: "))
print(f"Media de {nums} = {statistics.mean(nums)}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = str(int(input("10) Ingresar un entero: ")))
longitud = len(num)
mun = ""
for i in range(longitud):
    mun += num[longitud - i - 1]
print(f"{num} -> {mun}")