# una funcion es un tipo de instrucciones que nos permiten realizar una tarea especifica
#ayudan a evitar codigo repetido


#supongamos que queremos repetir una instruccion n veces, seria muy tedioso repetir y escribir el mismo codigo

"""name = "juancho"
apellido = "dominguez"
print((name + apellido)*5)"""

# se debe de definir para crear una funcion  el keyboard def
#para que se muestre el retorno debemos de imprimir la funcion porque sino no se vera en este caso el mensaje "hola"
def nombreApellido():
   print("jorge")
   print("dominguez")
   print("juancho")
   return "hola"

nombreApellido()

print("-----------------------------------------------------------------")
print(nombreApellido())

print("-----------------------------------------------------------------")
#funcion con parametro, queremos calcular si el sueldo que recibe un trabajador es menor o mayor que el salario minimo

def sueldoMinimo(sueldo) :
   if sueldo >= 1000:
      print("su sueldo es superior o igual al sueldo minimo")
   else: 
      print("lo estan tumbando en el camello, gana menos del sueldo minimo")
      
sueldoMinimo(800)