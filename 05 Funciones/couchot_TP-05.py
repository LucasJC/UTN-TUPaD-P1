# 1)
def imprimir_hola_mundo():
    print("Hola Mundo")
imprimir_hola_mundo()

# 2)
def saludar_usuario(nombre: str) -> None:
    print(f"Hola, {nombre}!")
saludar_usuario(input("¿Cuál es tu nombre? "))

# 3)
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")  
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = int(input("¿Cuántos años tienes? "))
residencia = input("¿Cuál es tu residencia? ")
informacion_personal(nombre, apellido, edad, residencia)

# 4)
def calcular_area_circulo(radio: float) -> float:
    pi = 3.14159
    area = pi * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio: float) -> float:
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# 5)
def segundos_a_horas(segundos: int) -> float:
    return segundos / 3600
segundos = int(input("Ingresar cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

# 6)
def tabla_multiplicar(numero: int) -> None:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingresar un número: "))
tabla_multiplicar(numero)

# 7)
def operaciones_basicas(a: int, b: int) -> dict:
    return {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b if b != 0 else "Error: División por cero"
    }
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"{resultados}")

# 8)
def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# 9)
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C es igual a {fahrenheit}°F")

# 10)
def calcular_promedio(a: int, b: int, c: int) -> float:
    return (a + b + c) / 3 
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
