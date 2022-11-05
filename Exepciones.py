# error en tiempo de ejecucion  (durante la ejecucion de un prgrama) x/0

num1 = 20
num2 = 2

print ("la division de {0}  entre {1} es: {2}".format(num1, num2, num1/num2))


"""try:
    resultado = num1/num2
except:
    print ("error de ejecucion de un prgrama")

print ("aqui termina mi programa")

try:
    resultado = num1/num2
except ZeroDivisionError:
    print ("no se puede dividir por cero")
finally:
    print ("siempre se ejecuta")
print ("aqui termina mi programa")

# finally, siempre se ejecuta independientemente de si se ejecuta el bloque try o no, util cuando se quiere mostrar algo."""