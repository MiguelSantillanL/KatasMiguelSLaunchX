'''

# Ejercicio 1: Transformar cadenas
Hay varias operaciones que puedes realizar en las cadenas cuando las manipulamos. En este ejercicio, usarás métodos de cadena 
para modificar el texto con hechos sobre la Luna y luego extraerás información para crear un breve resumen.

> **Nota**
> Dedica unos minutos a tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver si has 
logrado compilar el programa de acuerdo con las especificaciones.
'''

from turtle import title


print("Ejercicio 1\n")

#El texto con el que trabajarás es el siguiente: 

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
    On average, the v moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight 
    temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:

textSplit = text.split('. ')

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
# Define las palabras pista: average, temperature y distance suenan bien
keywords = ['average','temperature','distance']

#Cre un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
for i in textSplit:
    for j in keywords:
        if j in i:
            print(i)
            break

#Finalmente, actualiza el bucle(ciclo) para cambiar _C_ a _Celsius_:

# Ciclo para cambiar C a Celsius
for i in textSplit:
    for j in keywords:
        if j in i:
            print(i.replace(' C', ' Celsius'))
            break


print("\nEjercicio 2\n")

'''

# Ejercicio 2: Formateando Cadenas

Saber cómo dar formato a las cadenas es esencial cuando se presenta información de un programa. Hay algunas maneras diferentes de lograr esto en Python. En este ejercicio, se utilizan variables que contienen datos clave sobre la gravedad en varias lunas y luego se utilizan para dar formato e imprimir la información.

El formato tiene que acomodar información sobre otras lunas, por lo que debe ser genérico.

En lugar de reemplazar las variables en una cadena larga como parte de un párrafo, utiliza la información para presentarla en un formato tabular. El resultado debería verse así:

```
Gravity Facts about Ganymede
-------------------------------------------------------------------------------
Planet Name: Mars
Gravity on Ganymede: 1.4300000000000002 m/s2
```

'''

# Datos con los que vas a trabajar
name = "Mars"
gravity = 0.00143 # in kms
planet = "Ganímedes"


'''
Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra 
y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir.
'''
title = "\tGravity Facts about " + planet

'''
Ahora crea una plantilla de cadena multilínea para contener el resto de la información. En lugar de usar kilómetros, 
debes convertir la distancia a metros multiplicando por 1,000.
'''

plantilla = "\n" + "-"*80 + "\nPlanet Name: " + name + "\nGravity on " + planet + ": " + str(gravity*1000) + " m/s^2 "

'''
Finalmente, usa ambas variables para unir el título y los hechos.
'''
dataPlanet = title + plantilla

print(dataPlanet)

'''
Ahora usa información de una luna diferente para ver si la plantilla todavía funciona.

Datos muestra: 
```
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
```

'''

# Nuevos datos muestra

name = "Mars"
gravity = 0.00143 # in kms
planet = "Ganímedes"

print(plantilla)


'''

La salida no muestra información sobre Marte. Todavía muestra información sobre la Luna. Esto sucede porque las cadenas f están ansiosas en su evaluación, 
por lo que las variables una vez asignadas no se pueden reasignar. 
Para evitar este problema, vuelva a hacer la plantilla para utilizar .format():
'''

newTemplate = """
Gravity Facts about : {planet}
---------------------------------------------------------------------------------
Planet Name: {name}
Gravity on {planet}: {gravity} m/s^2
"""

print(newTemplate.format( planet = planet ,name = name , gravity = gravity))


'''
Debido a que .format() no permite expresiones, la gravedad en Ganímedes es incorrecta. Asegúrese de que la operación se realiza fuera de la plantilla de formato e 
imprima de nuevo para ver el resultado de trabajo.
'''
# Pista: print(nueva_plantilla.format(variables))
print(newTemplate.format( planet = planet,name = name, gravity = (gravity*1000) ))