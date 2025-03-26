# Programación 1 - TP1
# Alumno: Lucas Couchot

def tp1_1():
    print("Punto 1")
    print("Hola Mundo!")

def tp1_2():
    print("Punto 2")
    nombre = input("Ingresar nombre: ")
    print(f"Hola {nombre}!")

def tp1_3():
    print("Punto 3")
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    edad = input("Ingresar edad: ")
    residencia = input("Ingresar residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def tp1_4():
    import math
    print("Punto 4")
    radio = int(input("Ingresar el radio del círculo: "))
    print(f"Círculo de radio {radio}: Área {math.pi * (radio ** 2)}, Perímetro {2 * math.pi * radio}")

def tp1_5():
    print("Punto 5")
    segundos = int(input("Ingresar segundos: "))
    print(f"{segundos} segundos equivalen a {segundos / (60 * 60)} horas")

def tp1_6():
    print("Punto 6")
    num = int(input("Ingresar un número: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

def tp1_7():
    print("Punto 7")
    num1 = int(input("Ingresar un número: "))
    num2 = int(input("Ingresar otro número: "))
    print(f"Suma: {num1 + num2}; División: {num1 / num2}; Multiplicación: {num1 * num2}, Resta: {num1 - num2}")

def tp1_8():
    print("Punto 8")
    altura = float(input("Ingresar altura"))
    peso = int(input("Ingresar peso: "))
    print(f"Tu IMC es {peso / (altura * altura)}")

def tp1_9():
    print("Punto 9")
    temp = int(input("Ingresar temperatura en Celsius: "))
    print(f"{temp}°C equivale a {9/5*temp + 32}° Fahrenheit")

def tp1_10():
    print("Punto 10")
    num1 = float(input("Ingresar primer número: "))
    num2 = float(input("Ingresar segundo número: "))
    num3 = float(input("Ingresar tercer número: "))
    print(f"El promedio entre {num1}, {num2} y {num3} es {(num1 + num2 + num3) / 3}")

# Ejecución de todas las funciones
tp1_1()
tp1_2()
tp1_3()
tp1_4()
tp1_5()
tp1_6()
tp1_7()
tp1_8()
tp1_9()
tp1_10()