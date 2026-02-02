# función round()
# La función round() redondea un número flotante al entero más cercano
# o al número de decimales especificado.
# Sintaxis:
# round(numero, ndigits)
# Parámetros:
# numero: El número flotante que se desea redondear.
# ndigits (opcional): El número de decimales al que se desea redondear.
# Si se omite, se redondea al entero más cercano.
# Ejemplos de uso:
# Redondear al entero más cercano
print(round(3.6))  # Salida: 4
print(round(3.4))  # Salida: 3
# Redondear a un número específico de decimales
print(round(3.14159, 2))  # Salida: 3.14
print(round(2.71828, 3))  # Salida: 2.718
# Notas:
# Si el número está exactamente a mitad de camino entre dos enteros,
# round() redondea al entero par más cercano. Por ejemplo:
print(round(2.5))  # Salida: 2
print(round(3.5))  # Salida: 4          