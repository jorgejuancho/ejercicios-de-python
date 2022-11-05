# condicional if y else
from multiprocessing.managers import SharedMemoryManager

# importante conservar la identacion para que la funcion se pueda ejecutar sin error
#los dos puntos vendrian siendo el entonces
# else es opcional
edad = int(input("cuantos años tienes? "))
semanasEdad = str(edad*12)
print(type(semanasEdad))
if edad >=18:
    print(" estas viejo, has vivivido mas de " + semanasEdad + " meses" )
           
else:
    print("aun eres joven y bello menor de edad")
          
