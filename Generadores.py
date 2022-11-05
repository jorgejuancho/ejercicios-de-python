#generadores: permite extraer valores de una funcion y almacenarlos de uno en uno en objetos iterables (que se pueden recorrer)
#sin la necesidad de almacenarlos  todos a la vez en la memoria ram de nuestro dispositivo
#palabra clave "yield" en generadores.
# para adicionar elemntos a una lista se hace con .append



"""def generadorMultiplos7(limite):
   numero = 1 
   listaNumeros = []
   
   while numero <= limite:
       listaNumeros.append(numero*7)
       numero = numero + 1
   return listaNumeros
       
print(generadorMultiplos8(10))"""
       
def generadorMultiplos8(limite):
    number = 1
    
    while number <= limite:
        yield number * 8
        # genera un objeto iterable
        number = number +1
    
obtieneMultiplos8 = generadorMultiplos8(10)   

print(obtieneMultiplos8)


"""for n in obtieneMultiplos8: 
    print(n)"""
    
# la funcion next () nos retorna el siquiente elemento de un objeto iterable
print(next(obtieneMultiplos8))
print("aca hay 51 lineas de codigo " )
print(next(obtieneMultiplos8))
print("aca hay 82 lineas de codigo " )
print(next(obtieneMultiplos8))

# son mas eficientes que las funciones tradicionales
# son utiles en listas infinitas
# entre llamada y llamada de un objeto iterable este entra en un estado de pausa
