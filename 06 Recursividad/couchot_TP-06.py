# 1)
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("No definido para números negativos")
    elif num == 0 or num == 1:
        return 1
    else:
        return factorial(num - 1) * num
max = int(input("Ingrese un número entero: "))
for i in range(1, max + 1):
    print(f"El factorial de {i} es {factorial(i)}")

# 2)
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
max = int(input("Ingrese un número entero: "))
for i in range(1, max + 1):
    print(f"El número de Fibonacci en la posición {i} es {fibonacci(i)}")

# 3)
def potenciar(base: int, exponente: int) -> int:
    if exponente < 0:
        raise ValueError("No definido para exponentes negativos")
    elif exponente == 0:
        return 1
    else:
        return base * potenciar(base, exponente - 1)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {potenciar(base, exponente)}")

# 4)
def decimal_a_binario(num: int) -> str:
    if num < 0:
        raise ValueError("No definido para números negativos")
    elif num == 0:
        return "0"
    else:
        binario_actual = num % 2
        restante = num // 2
        return decimal_a_binario(restante) + str(binario_actual)

num = int(input("Ingrese un número entero: "))
print(f"El número {num} en binario es {decimal_a_binario(num)}")


# 5)
def es_palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

# 6)
def suma_digitos(n: int) -> int:
    if n == 0:
        return 0
    else:
        digito = n % 10
        restante = n // 10
        return digito + suma_digitos(restante)

entero = int(input("Ingrese un entero: "))
print(f"La suma de los dígitos de {entero} es {suma_digitos(entero)}")

# 7)
def contar_bloques(n: int) -> int:
    if n == 0:
        return 0
    else:
        print(n * ["#"])
        return n + contar_bloques(n - 1)
bloques_iniciales = int(input("Ingrese la cantidad de bloques iniciales: "))
bloques_totales = contar_bloques(bloques_iniciales)
print(f"La cantidad total de bloques es: {bloques_totales}")

# 8)
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if numero == digito else 0
    else:
        digito_actual = numero % 10
        restante = numero // 10
        if digito_actual == digito:
            return 1 + contar_digito(restante, digito)
        else:
            return contar_digito(restante, digito)      
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")