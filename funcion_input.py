# La función input() es capaz de leer datos que fueron introducidos por el usuario
# y pasar esos datos al programa en ejecución.

# Puede ser invocada sin argumentos. Ésta es la manera más sencilla de utilizar la función.
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")
# En este ejemplo, la función input() muestra el mensaje "¿Cuál es tu nombre? "
# y espera a que el usuario ingrese su nombre. Una vez que el usuario presiona  Enter,
# el valor ingresado se almacena en la variable nombre y luego se imprime un saludo personalizado.

# El resultado debe ser asignado a una variable; esto es crucial,
# si no se hace los datos introducidos se perderán.

# La función input() siempre devuelve una cadena de texto (str).

# Si se necesita otro tipo de dato, como un número entero o un número de punto flotante.
# #Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema,
# aquí están: int() y float().

edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)  # Convertir la cadena a un entero
print("El próximo año tendrás " + str(edad + 1) + " años.")
# En este ejemplo, la entrada del usuario se convierte de cadena a entero
# para poder realizar operaciones matemáticas con ella. Luego,
# se convierte de nuevo a cadena para la concatenación en la impresión final.