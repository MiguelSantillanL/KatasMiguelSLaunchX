# Ejercicio: Uso de funciones en Python

### Ejercicio 1: Trabajar con argumentos en funciones
print("Ejercicio 1: Trabajar con argumentos en funciones")

'''
Los argumentos requeridos en las funciones se utilizan cuando las funciones necesitan que esos argumentos funcionen correctamente. En este ejercicio, 
construirás un informe de combustible que requiere información de varias ubicaciones de combustible en todo el cohete.
'''

'''
> **TIP**
> Dedica unos minutos para tratar de encontrar una solución. Luego desplázate hacia abajo hasta la parte inferior para ver si has logrado compilar el programa
 de acuerdo con las especificaciones
Comienza por crear una función que necesite tres lecturas de combustible y devuelva un informe:
'''

# Función para leer 3 tanques de combustible y muestre el promedio

def tankReport(tank1, tank2, tank3):
    prom = (tank1 + tank2 + tank3) / 3
    return f"""The about the tanks:
    Tank1: {tank1}%
    Tank2: {tank2}%
    Tank3: {tank3}%
    Promedio: {prom}% 
    """

'''
Ahora que hemos definido la función de informes, vamos a comprobarlo. Para esta misión, los tanques no están llenos:
'''
# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(tankReport(30, 40, 50))

'''
En lugar de simplemente crear el informe, la función también está calculando el promedio. Mejora la legibilidad extrayendo el cálculo promedio de la
función en una nueva función para que el promedio se pueda hacer de forma independiente:
'''
# Función promedio 
def Promedio(val):
    return ( sum(val)/len(val) )


#Ahora actualiza la función de informes para llamando a la nueva función del promedio:
def tankReport(tank1, tank2, tank3):
    return f"""The about the tanks:
    Tank1: {tank1}%
    Tank2: {tank2}%
    Tank3: {tank3}%
    Promedio: {Promedio([tank1, tank2, tank3])}% 
    """

print(tankReport(60, 70, 80))

## Ejercicio 2: Trabajo con argumentos de palabra clave
print("Ejercicio 2: Trabajo con argumentos de palabra clave")

'''
### Ejercicio : Trabajar con argumentos de palabras clave en funciones
En este ejercicio, construirás un informe de cohete que requiere varias piezas de información, como el tiempo hasta el destino, el 
combustible a la izquierda y el nombre del destino. Comienza por crear una función que creará un informe preciso de la misión:
'''
'''
tiempo hasta el destino
combustible
destino
'''



# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def m_report(pre_launch_time, flight_time, destination, tank1, tank2):
    return f"""\tMission Report
    Mission to {destination}
    Total time: {pre_launch_time + flight_time} minutes
    Total fuel left: {tank1 + tank2} gallons
    """

'''
La función es problemática porque no se puede adaptar para minutos adicionales o tanques adicionales de combustible. Hazlo más flexible 
permitiendo cualquier número de pasos basados en el tiempo y cualquier número de tanques. En lugar de usar `*args` y `**kwargs`, aprovecha 
el hecho de que puedes usar cualquier nombre que desees. Asegurate que la función sea más legible mediante el uso de nombres de variables 
que están asociados con las entradas, como `*minutes` y `**fuel_reservoirs`:
'''
# Escribe tu nueva función de reporte considerando lo anterior
def m_report(destination, *time_min, **fuel):
    return f"""
    Mission to {destination}
    Total travel time: {sum(time_min)} minutes
    Total fuel left: {sum(fuel.values())}
    """

print(m_report("Mars", 10, 15, 51, tank1=56000, tank2=23000))


'''
Debido a que el combustible que queda en los tanques es específico de cada tanque, actualiza la función para usar el nombre de cada tanque en el informe:
'''
# Escribe tu nueva función
def m_report(destination, *time_min, **fuel):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(time_min)} minutes
    Total fuel left: {sum(fuel.values())}
    """
    for tank_name, gallons in fuel.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print(m_report("Mars", 10, 15, 51, tank1=56000, tank2=23000))