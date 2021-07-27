# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# Verifique cual cual de los dos textos es mayor alfabéticamente
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("El mayor textos es texto_1: {}".format(texto_1))

else:
    print("El mayor es texto_2: {}".format(texto_2))

# Transforma esas variables tipo texto y almacénalas
# en nuevas variables númericas (int)
# Repita el proceso, ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

texto_1 = int(texto_1)

texto_2=int(texto_2)

if texto_1 > texto_2:
    print("El mayor textos es texto_1: {}".format(texto_1))

else:
    print("El mayor es texto_2: {}".format(texto_2))


# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

#La respuesta es que en la tabla ASCII tienen el mismo valor
# por eso siempre texto_2 es mayor que texto_1 en los dos casos
