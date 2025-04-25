print("1)")
lista = range(4, 100, 4)
for i in lista:
    print(i)

print("2)")
lista = ["a", "b", "penultimo", "d"]
print(lista[-2])

print("3)")
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("!")
for i in lista_vacia:
    print(i)

print("4)")
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
for i in animales:
    print(i)

print("5)")
print("El programa elimina el elemento más grande y luego imprime la lista resultante.")

print("6)")
lista = range(10, 31, 5)
for i in lista[0:2]:
    print(i)

print("7)")
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "golf"
autos[2] = "duster"

print("8)")
lista_vacia = []
lista_vacia.append(5 * 2)
lista_vacia.append(10 * 2)
lista_vacia.append(15 * 2)
for i in lista_vacia:
    print(i)

print("9)")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
for i in compras:
    print(i)

print("10)")
lista_anidada = [ 15, True, [ 25.5, 57.9, 30.6 ], False ]
for i in lista_anidada:
    print(i)