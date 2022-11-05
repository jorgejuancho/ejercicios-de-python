#cuando indicamos un asterico delante del parametro de una funcion, estamos indicando que se va a recibir un numero indeterminado de parametros
#esos parametros se recibiran en forma de tupla

""""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
        
lenguajesObtenidos = devuelveLenguajes("python", "javascript","php","java","ruby")

print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))"""

# esta forma seria similar a un array bidimensional en otros lenguajes de programacion, usando for anidado
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra
        
lenguajesObtenidos = devuelveLenguajes("python", "javascript","php","java","ruby")

print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))

#python tiene su propia forma de hacer esto mediante yield from  que lo que hace es crear un objeto iterable dentro de otro objeto iterable. 

def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng
        
lenguajesObtenidos = devuelveLenguajes("python", "javascript","php","java","ruby")

print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))
print (next(lenguajesObtenidos))