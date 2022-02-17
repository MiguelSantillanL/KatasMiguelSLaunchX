# Ejercicio 1: Creación de diccionarios de Python

print("Ejercicio 1: Creación de diccionarios de Python")

'''
### Ejercicio: Crear y modificar un diccionario de Python

Los diccionarios python te permiten modelar datos más complejos. Los diccionarios son una colección de pares clave/valor, 
y son muy comunes en los programas Python. Su flexibilidad le permite trabajar dinámicamente con valores relacionados sin tener que crear clases u objetos.

Un diccionario se indica en Python mediante el uso de llaves (`{ }`), con pares clave/valor separados por dos puntos (`:`). 
Las claves son literales de cadena y los valores pueden ser de cualquier tipo de datos.{ }:

```python
demo = {
    'key': 'value',
    'number': 42
}
```

Para este ejercicio, crearás un diccionario que almacene información sobre el planeta Marte.


> **TIP**
> Dedica unos minutos para tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver 
si has logrado compilar el programa de acuerdo con las especificaciones

Agrega el código para crear un nuevo diccionario denominado 'planet'. Rellena con la siguiente información:

```
name: Mars
moons: 2
```
'''

planet = {
    'name': 'Mars',
    'moons': 2
}

#Para recuperar valores, puede utilizar el método  `get` o corchetes (`[ ]`) con el nombre de la clave que desea recuperar.

print("The planet is " , planet["name"] , " and has " , planet.get('moons') , " moons" )

'''
Puedes actualizar las claves existentes o crear otras nuevas utilizando el método `update` o entre corchetes (`[ ]`). 
Cuando se usa `update`, se pasa un nuevo objeto de diccionario con los valores actualizados o nuevos. Cuando se usan corchetes, 
se especifica el nombre de la clave y se asigna un nuevo valor.


```python
demo['new_key'] = 'New value'
```

Agrega un nuevo valor con una clave de 'circunferencia (km)'. Este nuevo valor debería almacenar un diccionario con las 
dos circunferencias del planeta:

```
polar: 6752
equatorial: 6792
```

'''

planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}


#Imprime el nombre del planeta con su circunferencia polar.
print("The planet " , planet["name"] , " has a polar circumference of " , planet["circunferencia (km)"]["polar"] )



## Ejercicio 2: Programación dinámica con diccionarios
print("Ejercicio 2: Programación dinámica con diccionarios")

### Ejercicio: Cálculo de valores
#En este escenario, calcularás tanto el número total de lunas en el sistema solar como el número promedio de lunas que tiene un planeta.


# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

'''
Los diccionarios de Python te permiten recuperar todos los valores y claves utilizando los métodos `values` y `keys`, 
respectivamente. Cada método devuelve una lista que contiene los datos, que luego se puede usar como una lista normal de Python.
 Puedes determinar el número de elementos mediante `len`, e iterar a través de él mediante un ciclo `for`.

Agrega el código a continuación para determinar el número de lunas. Comienza almacenando el valor `values` de `planet_moons` en una 
variable denominada `moons`. A continuación, almacena el número de planetas en una variable denominada `planets`.
'''

moons = planet_moons.values()

planets =  len(planet_moons.keys()) #N planets

'''
Agrega el código para contar el número de lunas. Puedes hacerlo creando un ciclo `for` para iterar a través de las lunas `moons` 
y agregándolos a una variable denominada `total_moons`. Finalmente calcule el promedio dividiendo `total_moons` por `planets` e imprimiendo los resultados.
'''

total_moons = 0
for i in moons:
    total_moons += i

Prom = total_moons / planets

print(Prom)