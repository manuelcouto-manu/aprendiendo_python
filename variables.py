# Las variables en Python son contenedores que almacenan datos o valores.
# Se crean al asignar un valor a un nombre utilizando el operador de asignación (=).
# Ejemplo de creación de variables:
mi_variable = 10          # Variable que almacena un entero
nombre = "Juan"          # Variable que almacena una cadena de texto
precio = 19.99           # Variable que almacena un número de punto flotante
es_activo = True         # Variable que almacena un valor booleano
# Reglas para nombrar variables en Python:
# 1. Los nombres de las variables deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
# 2. El resto del nombre puede contener letras, números (0-9) o guiones bajos.
# 3. Los nombres de las variables son sensibles a mayúsculas y minúsculas (case-sensitive).
# 4. No se pueden usar palabras reservadas de Python como nombres de variables.
# Ejemplos de nombres de variables válidos:
edad = 25
_nombre_usuario = "usuario123"
total_venta = 150.75

# PEP 8 -- Style Guide for Python Code recomienda la siguiente convención de nomenclatura
#  para variables y funciones en Python:

    # Los nombres de las variables deben estar en minúsculas,
    #  con palabras separadas por guiones bajos para mejorar la legibilidad (por ejemplo: var, mi_variable).
    # Los nombres de las funciones siguen la misma convención
    #  que los nombres de las variables (por ejemplo: fun, mi_función).
    # También es posible usar letras mixtas
    #  (por ejemplo: miVariable), pero solo en contextos donde ese ya es el estilo predominante,
    #  para mantener la compatibilidad retroactiva con la convención adoptada.

# Una variable se crea cuando se le asigna un valor, cualquier cosa puede ir dentro de una variable.

# Se puede utilizar print() para combinar   texto con variables
# utilizando el operador + para mostrar cadenas con variables, como por ejemplo:
nombre = "Ana"
edad = 30 # asigna 30 a edad # edad se convierte en 30.
print("Nombre: " + nombre + ", Edad: " + str(edad))

var = 1
print(var)
var = var + 1 # Toma el valor actual de la variable var, sumale 1 y guárdalo en la variable var.
print(var)