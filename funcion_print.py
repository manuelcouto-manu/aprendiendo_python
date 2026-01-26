print("¡Bienvenidos a Python!")
# Uso estándar (salto de línea automático)
print("Hola")
print("Mundo")

# Argumento: ¡Bienvenidos a Python! --> "Cadena de texto"
# Función: print() --> Imprime en pantalla el argumento proporcionado
# Descripción: Este código imprime un mensaje de bienvenida en la consola

# nombre_funcion(argumento) --> invoca la función con el argumento dado

# Una instrucción por linea es lo recomendado en Python

print() #Imprime una línea en blanco

print("¿Cómo estás?")

print() # Genera una línea vacía

print("Hoy es viernes \ny hace Sol") 

# Carácter de escape y nueva línea:
# \n es un carácter especial que indica un salto de línea

print("lunes","martes","miércoles") 

# Múltiples argumentos en print():
# Se pueden pasar varios argumentos separados por comas
# Genera la salida en una sola línea separados por espacios

print("Hoy es viernes, qué bien")
print("Fin de semana!")

# manera posicional de pasar argumentos
# print(arg1, arg2, arg3, ...)

# las instrucciones en el código se ejecutan en el mismo orden
# en que se colocaron en el archivo fuente

# argumentos de palabra clave (keyword arguments):

# Uso estándar (salto de línea automático)
print("Hola")
print("Mundo")

# Uso con argumento 'end' para mantener la misma línea
print("Hola", end=" ") # Debe ponerse después del último argumento posicional
print("Mundo") # Resultado: Hola Mundo

# Argumento de palabra clave 'sep' para cambiar el separador entre argumentos
print("lunes","martes","miércoles", sep=" - ")
# Resultado: lunes - martes - miércoles

# Ambos argumentos de palabras clave pueden mezclarse en una invocación