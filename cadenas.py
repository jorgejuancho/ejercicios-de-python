'''Escribir un  programa que pregunte el nombre del usuario en la consola y 
después de ser introducido por el usuario, muestre por pantalla <NOMBRE> 
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas 
y <n> es el número de letras que tienen el nombre.

nombre= input("ingrese su nombre de usuario:  ")

print("su nombre de usuario es " , nombre.upper()," el cual tiene ",  nombre.count('')-1, "  letras" )

El directorio telefónico de la empresa de aseo “Newclean” tiene el siguiente 
formato para  los números: prefijo-número-extensión donde el prefijo es el 
código  del  país  +34,  y  la  extensión  tiene  dos  dígitos  (por  ejemplo  +34-
913724710-56).  Escribir  un  programa  que  pregunte  por  un  número  de 
teléfono con este formato y muestre por pantalla el número de teléfono sin 
el prefijo y la extensión


telefono = input("ingrese el numero de telefono en el formato prefijo-número-extensión ")
x=telefono.split("-")

print(f"el numero de telefono es: {x[1]} "  )




   7. Escribir un programa que pregunte el correo  electrónico  del usuario en la 
consola y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @ pero con dominio ceu.es). '''

email=input("ingresa email ")

print(email[0:email.find('@')]+ "@ceu.es")

# 10.  Escribir  un  programa  que  pregunte  por  consola  por  los  productos  de  la 
# canasta familiar, separados por comas, y muestre por pantalla cada uno de 
# los productos en una línea distinta

# mercado = input("ingrese la lista del mercado separada por comas ")
# lista=mercado.split(",")
# print("el listado del mercado es: ")
# for i in lista:
#     print(i)
