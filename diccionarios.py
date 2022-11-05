# son estructuras de datos que nos permiten almacenar distintos valores
#los datos se almacenan asociados a una clave unica, relacion clave-valor
#los elementos almacenados estan en desorden

from logging.config import dictConfig


diccionar = {"colombia":"bogota","peru":"lima", "españa":"madrid"}
print(diccionar)

#buscar valor de una clave
print(diccionar["colombia"])

#adicionar objeto al dictionary
diccionar["venezuela"] = "caracas"
print(diccionar)

#reemplazar valor de una clave
diccionar["españa"] = "barcelona"
#borrar objeto del diccionar
del diccionar["españa"] 
print(diccionar)
# los valores pueden ser de varios tipos
diccionar2 = {"nombre":"juancho", "edad":"36", "salario":"0"}
print(diccionar2)

# objetos creados con diccionarios y tuplas, truco para que no se puedan modificar 
paises = ("rusia", "francia", "italia","portugal") #esto es una tupla
dicPaises = { paises[0]:"moscu", paises[1]:"paris", paises[2]:"roma", paises[3]:"lisboa"}
print(dicPaises)

#diccionario dentro de otro diccionario
lacteos = {"liquido1":"leche", "liquido2":"yogurt", "liquido3":"lecherita", "quesos":{1:"mozarella", 2:"holandes", 3:"fundido" }}
print(lacteos)
print(lacteos["quesos"])
# funcion get: buscar valor en un diccionario  pero si no lo encuentra devuelve el segundo valor del argumento, en nuestro ejemplo busca la llave lquido4 y como no esta devuelve el valor semen
print(lacteos.get("liquido4", "semen"))

# imprimir llaves de un diccionario con la funcion keys
print(lacteos.keys())

# imprimir LOS valores de un diccionario con la funcion values
print(lacteos.values())

#convertir diccionario a lista
valores = list(lacteos.values())
print(valores)

#convertir diccionario a tuple
valores2 = tuple(lacteos.keys())
print(valores2)
               