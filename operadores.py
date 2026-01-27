# Cuando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.
# Operadores aritméticos básicos en Python:
suma = 5 + 3            # Suma: resultado es 8
resta = 10 - 4          # Resta: resultado es 6
multiplicacion = 7 * 6  # Multiplicación: resultado es 42
division = 20 / 5       # División: resultado es 4.0 (siempre es flotante, en todos los casos!!)
division_entera = 20 // 6 # División entera: resultado es 3 (una división de entero entre entero da un resultado entero)
                            # el redondeo siempre es hacia abajo
modulo = 10 % 3        # Módulo: resultado es 1 (resto de la división)
exponente = 2 ** 3     # Exponente: resultado es 8 (2 elevado a la 3)   
# Operadores unarios y binarios
unario = -5                 # Unario: resultado es -5
binario = 10 + 5            # Binario: resultado es 15
#La diferencia entre operadores unarios y binarios es que los unarios operan sobre un solo operando,
# mientras que los binarios operan sobre dos operandos.

# 2 + 3 * 5     --> multiplicaciones preceden a las sumas: jerarquía de prioridades
print(9 % 6 % 2) # La expresión se evalúa de izquierda a derecha: resultado es 1
print(2 ** 2 ** 3) # Con exponente, la expresión se evalúa de derecha a izquierda: resultado es 256

# Prioridad de operadores (de mayor a menor):
# 1. Paréntesis: ()
# 2. Exponentes: **         
# 3. Multiplicación, División, División entera, Módulo: *, /, //, %
# 4. Suma y Resta: +, - 


# Operadores de comparación:
igual = (5 == 5)        # Igualdad: resultado es True
diferente = (5 != 3)    # Diferencia: resultado es True
mayor_que = (7 > 4)     # Mayor que: resultado es True
menor_que = (2 < 6)     # Menor que: resultado es True
mayor_o_igual = (5 >= 5) # Mayor o igual: resultado es True
menor_o_igual = (3 <= 4) # Menor o igual: resultado es True
# Operadores lógicos:
y_logico = (True and False)  # AND lógico: resultado es False
o_logico = (True or False)    # OR lógico: resultado es True
no_logico = not True          # NOT lógico: resultado es False    
