# Ejercicio1 - Utilizar operadores aritméticos
print("Ejercicio1 - Utilizar operadores aritméticos")

'''
### Operadores aritméticos en Python
Python proporciona operadores aritméticos comunes para que puedas realizar operaciones matemáticas en tu código. Estos incluyen las cuatro operaciones principales de 
suma, resta, multiplicación y división.

Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas.  Comenzaremos usando dos distancias de planetas: Tierra (149.597.870 km) 
y Júpiter (778.547.200 km).

> **TIP**
> Dedica unos minutos a tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver si has logrado compilar el programa de acuerdo 
con las especificaciones.

**Nota:** Quita las comas cuando uses los valores.
'''

# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

disTierra = 149597870 # in km
disJupiter = 778547200 # in km

'''
### Realizar la operación

Con los valores obtenidos, es el momento de añadir el código para realizar la operación. Restarás el primer planeta del segundo para determinar la distancia en kilómetros. 
A continuación, puedes convertir la distancia del kilómetro en millas multiplicándola por `0.621`.
'''

distancia = 0.621*( disJupiter - disTierra )
print(distancia)


print("Ejercicio 2: convierte cadenas en números y usa valores absolutos")
'''
## Ejercicio 2: convierte cadenas en números y usa valores absolutos

### Crear una aplicación para trabajar con números y entrada de usuario
Con frecuencia, deberás convertir los valores de cadena en números para realizar correctamente diferentes operaciones o determinar el valor absoluto de un número.

Para crear nuestra aplicación, queremos leer la distancia del sol para dos planetas, y luego mostrar la distancia entre los planetas. Haremos esto usando `input` 
para leer los valores, `int` para convertir a entero y luego `abs` para convertir el resultado en su valor absoluto.
'''

### Lee los valores
#Usando `input`, agrega el código para leer la distancia del sol para cada planeta, considerando 2 planetas.
### Convertir a número
#Debido a que `input` devuelve valores de cadena, necesitamos convertirlos en números. Para nuestro ejemplo, usaremos `int`

disPlanet1 = int(input('Distancia del sol al primer planeta: '))
disPlanet2 = int(input('Distancia del sol al segundo planeta: '))

### Realizar el cálculo y convertir a valor absoluto
'''
Con los valores almacenados como números, ahora puedes agregar el código para realizar el cálculo, restando el primer planeta del segundo. Debido a que el segundo planeta podría 
ser un número mayor, usarás `abs` para convertirlo a un valor absoluto. También agregarás el código para mostrar el resultado en millas multiplicando la distanciwqewqe del kilómetro por 0.621
'''
# Realizar el cálculo y determinar el valor absoluto
disKm = disPlanet2 - disPlanet1
print("La distancia es " + str(disKm) + "km")
print("La distancia es " + str(abs(disKm*0.621)) + " mi")


### Prueba tu aplicación
'''
Para probar el proyecto, ejecuta tu notebook. En la parte superior de vscode surgirá un cuadro de diálogo para que proporciones las distancias. Puede utilizar los datos de la tabla siguiente:

| Planeta  | Distancia al sol  |
| -------  | ----------------- |
| Mercurio | 57900000          |
| Venus    | 108200000         |
| Tierra   | 149600000         |
| Marte    | 227900000         |
| Júpiter  | 778600000         |
| Saturno  | 1433500000        |
| Urano    | 2872500000        |
| Neptuno  | 4495100000        |

'''
