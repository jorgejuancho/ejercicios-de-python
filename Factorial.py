# factorial: es el producto de todos los numeros enteros comprendidos entre el uno y el numero dado
#ejemplo factorial de 5!= 1x2x3x4x5 = 120

def facto(num):
    factorial = 1
    for num in range(1, num+1):
        factorial = factorial*num
    return factorial

num =int(input("dame  el numero que deseas calcular el factorial: "))

print(f"el factorial del numero {num} es:  = {facto(num)}")


