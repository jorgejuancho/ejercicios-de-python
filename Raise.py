# raise: sirve para ejecutar de forma intencional excepciones en python, genera que se caiga voluntariamente el programa
# if:si, elif:sino, else:en otro caso

def evaluarNota (nota):
    if nota <= 0: 
       raise ZeroDivisionError("no se permiten valores negative")
    elif nota >= 16:
        print ("exelente")
    elif nota >= 11:
        print ("aprobado")
    else: 
        print ("reporbado")
        
evaluarNota(-2)