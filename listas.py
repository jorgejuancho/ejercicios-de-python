# listas de datos que nos permiten almacenar valores
#son equivalentes a los arrays en otros lenguajes de programacion
#son estructuras dinamicas que pueden cambiar valores, diferentes a las tuplas que son inmutables

lista1 = ["mierda", 2, 3.14, True, False, 100]
print(lista1)
lista2 = [-1,-3, 5.4, 28.00]
print(lista1[-1])
print(lista1[1:3])
#insertar objetos
lista1.append("juancho")
print(lista1)
#insertar objetos en una posicion determinada
lista1.insert(3,"angela")
print(lista1)

#extender lista 
lista2.extend(["eso", "es","puro", "text"])
print(lista2)

#eliminar objeto de la lista
lista2.remove("eso")
print(lista2)

#eliminar el ultimo elemento de la lista con .pop

print(lista1)
lista1.pop()
print(lista1)

#multiple list
print(lista2*3)
#plus  lista
print(lista1+lista2)
print(lista2+lista1)

#buscar elemento en lista true or false 
print("carro" in lista1)
print(3.14 in lista1)

