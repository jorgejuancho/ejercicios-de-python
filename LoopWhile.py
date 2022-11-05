"""estructura repetitiva que nos permite realizar multiples iteraciones basandonos en el resultado de una expresion logica, esa exprecion logica puede tener como resultado True o False, se detiene cuando deja de cumplirse la condicion inicial"""

i = 1
while i < 10:
    print ("valor actual {0}".format(i))
    i=i+1
print ("hemos terminado el loopWhile")

indice = 0

while indice <= 40 :
    print("numero {0}".format(indice))
    indice = indice + 2
    
print ("hemos terminado la impresion de numero pares desde el 0 hasta el 40")