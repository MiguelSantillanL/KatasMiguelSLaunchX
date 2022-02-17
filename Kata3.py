'''
# Ejercicio - Escribir declaraciones `if`, `else`, y `elif`

Las instrucciones `If` te permiten ejecutar condicionalmente código Python. Se usan comúnmente en Python para "tomar decisiones" sobre lo que debería suceder a continuación mientras se ejecuta un programa.

Para crear una instrucción `if` en Python, define una expresión de prueba que pueda tener un valor `True` o `False`, seguido de un bloque de código con sangría que se ejecutará si se cumple la condición.  

```python
if expresion_prueba:
    # intrucción(es) a ejecutar
```

Para escribir un programa con una lógica condicional más compleja, puedes agregar instrucciones `else` y `elif` al bloque de código. También puedes anidar instrucciones condicionales. 


```python
if expresion_prueba:
    # intrucción(es) a ejecutar
    if expresion_prueba:
        # intrucción(es) a ejecutar
    else: 
        # intrucción(es) a ejecutar
elif expresion_prueba:
    # intrucción(es) a ejecutar
else:
    # intrucción(es) a ejecutar
```

> **TIP**
> Dedica unos minutos a tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver si has logrado compilar 
el programa de acuerdo con las especificaciones.

Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido. La velocidad 
del asteroide varía dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.

Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

'''

print("\n\tEjercicio 1:")
asteroide = int(input("Velocidad del asteroide: "))
if (asteroide > 25):
    print('\t¡¡¡ALERTA!!! \n¡¡¡Se acerca un asteroide !!!')
else:
    print('¡Todo normal, sin peligro!')


'''
Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra. 
Escribe la lógica condicional que usa declaraciones `if`, `else`, y `elif` para alertar a las personas de todo el mundo que deben buscar un asteroide en el cielo. 
¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!
'''

print("\n\tEjercicio 2:")
asteroide = int(input("Velocidad del asteroide: "))
if (asteroide > 19):
    print('\t!!!MIRA AL CIELO!!! \n!Hay luces en el cielo!')
else:
    print('¡Todo normal!')

'''
# Ejercicio: Uso de operadores `and` y `or` 

En el ejercicio anterior, trabajó con sentencias `if`, `else`, y `elif` para escribir programas con lógica condicional compleja. 
Para crear expresiones booleanas aún más interesantes, puede usar los operadores `and` y `or` en Python.

Las expresiones `and` son sólo si ambas subexpresiones son verdaderas.

`expresión1 and expresión2`

Las expresiones `or` son `True` si *al menos una* subexpresión es verdadera.

`expresión1 or expresión2`

En este ejercicio, aprenderás información más matizada sobre cuándo los asteroides representan un peligro para la Tierra, y utilizarás esa información 
para mejorar nuestro sistema de advertencia. Aquí está la nueva información que necesitas saber:

*Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán a medida que entren en la atmósfera de la Tierra.
* Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.

También discutimos en el ejercicio anterior que:

* La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
* Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.

Usando toda esta información, escribe un programa que emita la advertencia o información correcta a la gente de la Tierra, según la velocidad y el tamaño de un asteroide. 
Utiliza instrucciones `if`, `else`, y `elif`, así como los operadores `and` y `or`.
'''

print("\n\tEjercicio 3:")
vel_Asteroide = int(input("Velocidad del asteroide: ")) #Velocidad asteroide
tam_Asteroide = int(input("Tamaño del asteroide: ")) #Tamaño del asteroide
if (vel_Asteroide) > 25 and (tam_Asteroide > 25):
    print('\t¡¡¡ALERTA!!! \n\t¡¡¡PELIGRO!!! \n¡¡¡Se acerca un asteroide muy peligroso !!!')
elif (vel_Asteroide > 19):
    print('\t!!!MIRA AL CIELO!!! \n!Hay luces en el cielo!')
else:
    print('¡Todo normal!')