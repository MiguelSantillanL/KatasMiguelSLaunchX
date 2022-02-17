# Ejercicio 1: Creación de un bucle "while"

print("Ejercicio 1: Creación de un bucle while")

'''
### Ejercicio 1: Uso de ciclos `while` en Python

En Python, los ciclos `while` te permiten ejecutar código un número desconocido de veces. Los ciclos examinan una condición booleana y, 
siempre que la condición sea verdadera, se ejecutará el código dentro del ciclo. Esto es muy útil para situaciones como solicitar valores a un usuario.

En este ejercicio, estás creando una aplicación que solicita a un usuario que ingrese una lista de planetas. En un ejercicio posterior, 
agregarás código que muestre la lista. Por ahora, crearás solo el código que solicita al usuario la lista de planetas.

> **TIP**
> Dedica unos minutos para tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver si has logrado compilar el 
programa de acuerdo con las especificaciones

Comienza agregando dos variables, una para la entrada del usuario, con el nombre `new_planet`, y otra variable para la lista de planetas, denominada `planets`.
'''

new_planet = ''
planets = []

'''
### Crea un ciclo `while`

Comenzando con las variables que acabas de crear, crearás un ciclo `while`. El ciclo `while` se ejecutará *mientras* el `new_planet` **no** sea igual a la palabra 'done'.

Dentro del ciclo, comprobarás si la variable `new_planet` contiene un valor, que debería ser el nombre de un planeta. Esta es una forma rápida de ver si el usuario 
ha introducido un valor. Si lo han hecho, tu código agregará (`append`) ese valor a la variable `planets`.


Finalmente, usarás `input` para solicitar al usuario que ingrese un nuevo nombre de planeta o que escriba *done* si ha terminado de ingresar nombres de planeta.
 Almacenará el valor de `input` en la variable `new_planet`.
'''

while (new_planet.lower() != 'done'):
    if new_planet:
        planets.append(new_planet)
    new_planet = input('New planet: ')



## Ejercicio 2: Creación de un ciclo "for"

'''
### Ejercicio: - Ciclo para una lista

En el ejercicio anterior, creaste código para solicitar a los usuarios que introduzcan una lista de nombres de planetas. En este ejercicio, 
completarás la aplicación escribiendo código que muestre los nombres de esos planetas.

### Mostrar la lista de los planetas

La variable `planets` almacena los nombres de planeta que ha introducido un usuario. Ahora usarás un ciclo para mostrar esas entradas.

Crea un ciclo `for` para iterar sobre la lista `planets`. Puedes usar como nombre de la variable `planet` para cada planeta. Dentro del ciclo `for`, 
recuerda utilizar `print` para mostrar cada `planet`.
'''

for i in planets:
    print(i)