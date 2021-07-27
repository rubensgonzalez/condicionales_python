# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado
'''

temp1 = float(input("Ingrese la primer temperatura\n"))
temp2 = float(input("Ingrese la segunda temperatura\n"))
temp3 = float(input("Ingrese la tercera temperatura\n"))

if (temp1 > temp2) and (temp1 < temp3):
        print("La temperatura maxima ingresada es {}".format(temp1))
elif (temp2 > temp1) and (temp2 > temp3):
    print("La temperatura maxima ingresada es {}".format(temp2))
elif (temp3 > temp1) and (temp3 > temp2):
    print("La temperatura maxima ingresada es {}".format(temp3))
    
print("\n")

if (temp1 < temp2) and (temp1 < temp3):
        print("La temperatura minima ingresada es {}".format(temp1))
elif (temp2 < temp1) and (temp2 < temp3):
    print("La temperatura minima ingresada es {}".format(temp2))
elif (temp3 < temp1) and (temp3 < temp2):
    print("La temperatura minima ingresada es {}".format(temp3))
            
print("\n")        
prom= (temp1+temp2+temp3)/3
print("El promedio de las temperaturas ingresadas es:{}".format(prom))


print("\n")


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
