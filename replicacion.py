# El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena)
# se convierte en un operador de replicación.
repetido = "Hola! " * 3
print(repetido)  # Salida: Hola! Hola! Hola!    
# También funciona en el otro orden
repetido2 = 4 * "Adiós! "
print(repetido2)  # Salida: Adiós! Adiós! Adiós! Adiós! 
# Nota: El operador de replicación solo funciona cuando uno de los operandos es una cadena y el otro es un entero.
# Intentar usar un número de punto flotante (float) resultará en un error.
# Por ejemplo, la siguiente línea generaría un error:
# error_replicacion = "Error! " * 2.5  # Esto causará un TypeError