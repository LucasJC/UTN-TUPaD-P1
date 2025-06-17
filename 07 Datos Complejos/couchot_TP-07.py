# 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1) ", precios_frutas)

# 2)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2) ", precios_frutas)

# 3)
solo_precios = precios_frutas.values()
print("3) ", solo_precios)

# 4)
contactos = {}
cantidad_contactos = int(input("4) ¿Cuántos contactos querés cargar?: "))
for i in range(cantidad_contactos):
    nombre = input(f"Ingresar nombre del contacto {i}: ")
    telefono = input(f"Ingresar teléfono del contacto {i}: ")
    contactos[nombre] = telefono
nombre_buscado = input("Ingresar nombre de contacto a buscar: ")
if nombre_buscado in contactos:
    print(f"El teléfono de {nombre_buscado} es {contactos[nombre_buscado]}")
else:
    print(f"No se encontró el contacto {nombre_buscado}")

# 5)
palabras = input("5) Ingrese una frase: ").split()
palabras_unicas = set(palabras)
cantidad_palabras = {}
for palabra in palabras_unicas:
    cantidad_palabras[palabra] = palabras.count(palabra)
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {cantidad_palabras}")

# 6)
import statistics
alumnos = {}
print("6) Ingrese los datos de 3 alumnos:")
for i in range(3):
    nombre = input(f"Ingresar nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"- Ingresar nota {j+1} del alumno {i}: "))
        notas.append(nota)
    alumnos[nombre] = statistics.mean(notas)
print("Promedios:", alumnos)

# 7)
print("7)")
aprobaciones_parcial_1 = ["Carlos", "Julia", "Andrés"]
aprobaciones_parcial_2 = ["Julia",  "Andrés", "Pedro"]

set_alumnos = set()

dict_parcial_1 = {}
for i in range(len(aprobaciones_parcial_1)):
    dict_parcial_1[aprobaciones_parcial_1[i]] = i
    set_alumnos.add(aprobaciones_parcial_1[i])

dict_parcial_2 = {}
for i in range(len(aprobaciones_parcial_2)):
    dict_parcial_2[aprobaciones_parcial_2[i]] = i
    set_alumnos.add(aprobaciones_parcial_2[i])

alumnos_que_aprobaron_ambos = []
alumnos_que_aprobaron_uno = []
for alumno in set_alumnos:
    if alumno in dict_parcial_1 and alumno in dict_parcial_2:
        alumnos_que_aprobaron_ambos.append(alumno)
    elif alumno in dict_parcial_1:
        alumnos_que_aprobaron_uno.append(alumno)
    elif alumno in dict_parcial_2:
        alumnos_que_aprobaron_uno.append(alumno)

print("Alumnos que aprobaron ambos parciales:", alumnos_que_aprobaron_ambos)
print("Alumnos que aprobaron al menos uno de los parciales:", alumnos_que_aprobaron_uno)

# 8)
stock = {}
def elegir_operacion():
    print("Operaciones disponibles: Agregar stock (a), Consultar stock (c), Salir (s)")
    return input("Ingresar operacion: ").strip().lower()

while(operacion := elegir_operacion()) != "s":
    if operacion == "a":
        producto = input("\nNombre del producto: ")
        stock_actual = stock.get(producto, 0)
        print(f"Stock actual de {producto}: {stock_actual}")
        cantidad = int(input("Cantidad a agregar: "))
        stock[producto] = stock_actual + cantidad
        print("Stock agregado\n")
    elif operacion == "c":
        producto = input("\nNombre del producto: ")
        stock_actual = stock.get(producto, 0)
        print(f"Stock actual de {producto}: {stock_actual}\n")
    else:
        print("Operación no válida.")

# 9)
dia = input("9) Ingrese un día de la semana: ").strip().lower()
hora = input("Ingrese una hora (HH:MM): ").strip()
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
evento = agenda.get((dia, hora))
if evento:   
    print(f"Agenda para {dia, hora}: {evento}")
else:
    print(f"No hay eventos programados para {dia, hora}.")

# 10)
original = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago"}
invertido = {}
for pais, ciudad in original.items():
    invertido[ciudad] = pais
print("10) original:", original)
print("invertido:", invertido)
