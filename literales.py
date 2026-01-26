# Los literales son representaciones fijas de valores en el código fuente,
# Tipos comunes de literales en Python incluyen: 
# - Literales de cadena: cadenas de texto (str) delimitadas por comillas simples   
# - Literales numéricos: enteros (int), flotantes (float), complejos (complex)
# - Literales booleanos: True y False (bool)
# - Literales especiales: None (representa la ausencia de valor)    
# - Literales de colección: listas (list), tuplas (tuple), conjuntos (set), diccionarios (dict)
# Ejemplos de literales en Python:
cadena_literal = "Hola, Mundo!"  # Literal de cadena
entero_literal = 42               # Literal entero
flotante_literal = 3.14           # Literal flotante
booleano_literal = True           # Literal booleano
nulo_literal = None               # Literal especial
lista_literal = [1, 2, 3]        # Literal de lista
tupla_literal = (4, 5, 6)       # Literal de tupla
conjunto_literal = {7, 8, 9}     # Literal de conjunto
diccionario_literal = {"clave": "valor"}  # Literal de diccionario      
# Los literales son fundamentales para definir datos en programas Python

# Creación de comillas en literales de cadena:
comillas_simples = 'Esto es una cadena con comillas simples'  # Literal de cadena con comillas simples
comillas_dobles = "Esto es una cadena con comillas dobles"  # Literal de cadena con comillas dobles
comillas_simples_dentro = "Ella dijo: 'Hola'"  # Literal de cadena con comillas simples dentro
comillas_dobles_dentro = 'Él respondió: "¿Cómo estás?"'  # Literal de cadena con comillas dobles dentro
# Comillas con caracteres de escape:
comillas_simples_escape = 'It\'s a beautiful day'  # Literal de cadena con comillas simples usando escape
comillas_dobles_escape = "He said, \"Hello!\""  # Literal de cadena con comillas dobles usando escape



# Python permite el uso de guion bajo en los literales numéricos para mejorar su legibilidad:
gran_numero = 1_000_000_000  # Equivalente a 1000000000
pi_aproximado = 3.141_592_653  # Equivalente a 3.141592653

# Enteros: números octales y hexadecimales  
numero_octal = 0o12  # Equivalente a 10 en decimal
numero_hexadecimal = 0xA  # Equivalente a 10 en decimal 

# Flotantes: se usa el punto decimal para separar la parte entera de la fraccionaria
numero_flotante = 1234.5678  # Literal de punto flotante
# el valor de cero punto cuatro puede ser escrito en Python como:
cero_coma_cuatro = 0.4  # Literal de punto flotante
# se puede omitir el cero cuando es el único dígito antes del punto decimal.
cero_coma_cuatro_alternativo = .4  # Literal de punto flotante

# 4 es un número entero, mientras que 4.0 es un número punto-flotante   
entero_cuatro = 4      # Literal entero
flotante_cuatro = 4.0  # Literal de punto flotante
# Ambos representan el mismo valor numérico pero son de tipos diferentes
# Los literales son inmutables, es decir, su valor no puede cambiar durante la ejecución del programa

0.0000000000000000000001 # Literal de punto flotante muy pequeño
print(0.0000000000000000000001) # cuando se imprime en pantalla
# la salida será:
1e-22
# Python siempre elige la presentación más corta del número,
# y esto se debe de tomar en consideración al crear literales.

# boleanos:
verdadero = True   # Literal booleano verdadero, numero equivalente 1
falso = False     # Literal booleano falso, numero equivalente 0