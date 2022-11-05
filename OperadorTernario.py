
""" se usa para comentarios largos cuando etos son mayores a una linea
en otros lenguajes de progrmacion por ejemplo java o javascript para crear un operador ternario se haria de la siguiente manera:
sexo = 10>3 ? "masculino" : "femenino"  quiere decir que si se cumple la primera condicion de que 10 sea mayor de 3 entonces se asignara el sexo masculino, si es falso se asignara el sexo femenino """

# en pyton este problema se resuelve gracias a las tuplas a traves de la siguiente estrategia

sexos = ("hombre", "mujer")

sexo = sexos[1] # es mujer
print (sexo)
sexo = sexos[0] # es hombre
print (sexo)