# 1. convertir un valor numerico a texto

'''numero =  int(input("digite un numero entre el 1 y el 3 "))

if numero == 1:
 print("usted ha digitado el numero UNO ")
elif numero == 2:
    print("usted ha digitado el numero DOS ")
elif numero == 3: 
    print("usted ha digitado el numero TRES")
else: 
    print("usted ha  digitado un numero no valido ")   
    
# 2. solicitar el mes del año e indicar la estacion del mes en el que esta
if mes == "enero" or mes == "febrero" or mes == "diciembre":
    print(" estamos en invierno ")
elif mes == "marzo" or mes == "abril" or mes=="mayo": 
    print(" estamos en primavera")
elif mes == "junio " or mes == "julio" or mes=="agosto": 
    print(" estamos en otoño")
elif mes == "septiembre" or mes == "octubre" or mes=="noviembre": 
    print(" estamos en primavera")
else:
    print("mes no valido, solo se recibe el mes en minuscula")
    
    
# 3.	Etapas de la vida:
El usuario debe hacer un programa donde digite un rango de edad y le muestre:
a.	un valor de 0-10: "La infancia es fantástica"
b.	un valor de 10-20: "Muchos cambios y mucho estudio"
c.	un valor dd 20-30: "Amor y vida adulta

edad= int(input("ingrese la edad "))

if 0<=edad <=10:
    print("La infancia es fantástica")
elif 10<edad <=20:
     print("Muchos cambios y mucho estudio -->  ")
elif 20<edad <=30:
     print("Amor y vida adulta") 
else:
    print("edad no relacionada ")  
    
4.	Sistema de calificación:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario Digite una clasificación entre 0 y 10.
•	Si esta entre 8 y 10: imprimir una Excelente
•	Si esta entre 7 y menor a 8: imprimir una Muy bien 
•	Si esta entre 6 y menor a 7: imprimir una Bien
•	Si esta entre 0 y menor a 6: imprimir una Reprobado
•	cualquier otro valor debe imprimir: Valor incorrecto "

6.	Escriba un programa que almacene la cadena de contraseña en una variable, solicite la contraseña al usuario e imprima en la pantalla si la contraseña ingresada por el usuario coincide con la contraseña almacenada en la variable, independientemente de las letras mayúsculas y minúsculas.
password ="juancho"

contraseña = input("ingrese la contraseña ")


if password == contraseña.lower():
    print("contraseña correcta")
    
else:
    print("contraseña incorrecta") 

7.	Escriba un programa que le pida al usuario que ingrese dos números y muestre su división en la pantalla. Si el divisor es 0, el programa mostrará un error.
num1=float(input("ingrese el primer  numero "))
num2=float(input("ingrese el segundo numero2"))

if num2 ==0:
 print(" no esta permitida la division por cero")
else:
 print(" el resultado de la division es ", num1/ num2)



9.	Para pagar un determinado impuesto es necesario ser mayor de 16 años y tener unos ingresos iguales o superiores a 1.000 mensuales. Escriba un programa que le pregunte al usuario su edad e ingresos mensuales y muestre en la pantalla si el usuario tiene que pagar impuestos.

edad= int(input("ingrese la edad"))

ingreso=float(input("ingrese salario"))

if edad >16 and ingreso >=1000:
 print("debe de pagar impuestos")
else:
    print("no paga impuestos")


10.	Los alumnos de un curso se dividen en dos grupos A y B según sexo y nombre. El grupo A está formado por mujeres que llevan el nombre de M y hombres que llevan el nombre de N, y el grupo B es el resto. Escriba un programa que le pregunte al usuario su nombre y género y muestre el grupo correspondiente en la pantalla.'''




    
    
    
    
       
       
    
    