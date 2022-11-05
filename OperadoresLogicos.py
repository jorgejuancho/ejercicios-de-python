# operador logico and y significa: "y si ademas"
# operador logico or significa: "o sino"
# not significa: negacion

#ejercicio beneficio economico para la matricula del colegio

from sqlalchemy import false


beneficio = False
distancia = int(input('ingrese la distancia en metros que hay hasta el colegio: '))
hermanos = int(input('ingrese la cantidad de hermanos que estudian en el colegio: '))
salario = int(input('ingrese el sueldo de los padres: '))

if (distancia >= 2000 and hermanos >2) or ( salario <= 2500):
    beneficio = True
    print("tiene un descuento en la matricula del 25%")
else:
    print("debe de pagar el total de la matricula del colegio")