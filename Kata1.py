'''
Oficial superior> "¿Cadete?"

Usted > "¿Sí, señora?"

Oficial superior> "¿Puedes construir un programa que me muestre la fecha? La computadora del barco no venía con mucho en términos de programas de utilidad, por lo que necesitamos crear los que necesitamos. ¿Puedo confiar en ti con esto?"

Usted > "Considéralo hecho".

Oficial superior> "Excelente".

    ## Tu primer programa

Para crear este programa, deberás utilizar los conceptos que aprendiste en el último módulo. Usarás Jupyter Notebook en este ejercicio, que es una combinación de texto y código con la que puede interactuar. Finaliza el código siguiente para que el resultado muestre la fecha de hoy.
'''

from datetime import date

print("Today's date is: " , date.today())

'''
> **TIP**
> Dedique unos minutos a tratar de encontrar una solución. Luego desplácese hacia abajo hasta la parte inferior para ver si ha logrado compilar el programa de acuerdo con las especificaciones.

## Construir un convertidor de unidades

El oficial superior> "Necesito una cosa más: un programa de conversión entre parsecs y años luz. Tener un programa de este tipo podría ser realmente útil en el puente para trazar nuestro curso".

Tú> "¡Lo haré!"
'''

parsec = 11

lightyears = 3.26156

print(str(parsec) + " parsec, is " + str(lightyears*parsec) + " lightyears")