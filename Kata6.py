# Ejercicio1: Crear y usar listas de Python

print("Ejercicio1: Crear y usar listas de Python")

'''
### Ejercicio: Usar listas para almacenar nombres de planetas
Las listas permiten almacenar varios valores en una sola variable. 
Comenzarás un proyecto sobre información planetaria creando una lista de planetas.

> **TIP**
> Dedica unos minutos para tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte 
inferior para ver si has logrado compilar el programa de acuerdo con las especificaciones
'''

#En primer lugar, crea una variable denominada `planets`. Agrega los ocho planetas (sin Plutón) a la lista. A continuación, muestra el número de planetas.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

print("Num of planets: ", len(planets))


#Agrega a Plutón a la lista que creaste. Luego muestra tanto el número de planetas como el último planeta de la lista.
planets.append('Pluto')
print("Num of planets: ", len(planets) ," and " , planets[-1] ," is the last planet")



print("Ejercicio 2: Trabajando con datos de una lista")

## Ejercicio 2: Trabajando con datos de una lista

### Usar slices para recuperar partes de una lista

'''
Es posible que debas trabajar con diferentes secciones de una lista. En nuestro ejemplo, 
queremos mostrar planetas más cerca y más lejos del sol de un planeta que el usuario ingresa por teclado.

Comienza agregando el código para crear una lista con los planetas.
'''

# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

### Solicita al usuario el nombre de un planeta

'''
A continuación, agrega el código para solicitar al usuario un nombre. Debido a que las cadenas
 distinguen entre mayúsculas y minúsculas en Python, pídale al usuario que use una letra mayúscula para comenzar el nombre del planeta.
'''

planetName = input('Name of the planet (with a capital letter to start): ')

### Encuentra el planeta en la lista
'''
Para determinar qué planetas están más cerca que el que ingresó el usuario, debes encontrar dónde está el planeta en la lista. 
Puedes utilizar `index` para realizar esta operación. Agrega el código para encontrar el índice del planeta.
'''

planet_index = planets.index(planetName)

### Mostrar planetas más cercanos al sol que el que el usuario ingresó

'''
Con el índice determinado, ahora puedes agregar el código para mostrar los planetas más cercanos al sol.
'''

print('Planets closer than ' + planetName)
print(planets[:planet_index])

# Mostrar planetas más alejados del sol que el que el usuario ingresó

'''
Puedes usar el mismo índice para mostrar planetas más alejados del sol. Sin embargo, recuerda que el índice 
inicial se incluye cuando usas un slice. Como resultado, tendrás que agregar 1 al valor. Agrega el código para mostrar los planetas más alejados del sol.
'''

# Muestra los planetas más lejanos al sol

print('Here are the planets further than ' + planetName)
print(planets[(planet_index+1):])