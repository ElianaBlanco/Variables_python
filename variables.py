# Define una variable de cada tipo de primitivo
cadena = "Hola"
entero = 42
flotante = 3.14
booleano = True

# Concatena la cadena con las otras variables
resultado_concatenacion = cadena + str(entero) + str(flotante)

# Límites de enteros y flotantes en Python
"""
Los enteros en Python no tienen un límite máximo específico, pero están limitados por la memoria del sistema.
Los flotantes en Python siguen el estándar IEEE 754, por lo que tienen un límite de precisión finita. Pueden representar números muy grandes o muy pequeños, pero con una precisión limitada.
"""

# Fórmula para la suma de los primeros n números pares
n = 10 
suma_pares = n * (n + 1)

# Imprime los resultados
print("Concatenación:", resultado_concatenacion)
print("Límites de enteros y flotantes en Python:")
print("Suma de los primeros", n, "números pares:", suma_pares)