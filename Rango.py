# range():  crea una lista inmutable de numeros enteros en sucesion arismetica.

numeros = range(5) 
print (numeros[4])


numeros2 = range(4,10) 
# 4, 5, 6, 7, 8, 9 va siempre hasta n-1 ya que cuenta el cero
print (numeros2[5]) 
print (numeros2[1]) 

# el primer valor significa donde inicia la serie, el segundo valor hasta donde llega la serie y el ultimo valor nos indica el incremento. en el ejemplo el numero: 8

numeros3 = range(10,100,8)
print (numeros3[0])
print (numeros3[9])
