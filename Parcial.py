# Inicializamos la suma
suma = 0
i = 0  # Iniciamos el contador

# Recorremos 5 veces para leer 5 números
while i < 5:  # Mientras i sea menor que 5
    print("Ingrese el número", i + 1, ":")
    numero = int(input())

    # Verificamos si el número es positivo y par
    if numero > 0 and numero % 2 == 0:
        suma += numero

    i += 1  # Incrementamos el contador

# Mostramos el resultado
print("La suma de los números positivos y pares es:", suma)

# Pedir al usuario que ingrese la edad
edadUsuario = input("Ingrese la edad: ")

# Verificar si la entrada es un número decimal
if '.' in edadUsuario:
    print("Error: La edad debe ser un número entero positivo.")
else:
    # Convertir la entrada a entero y verificar si es un número entero positivo
    edad = int(edadUsuario)
    
    if edad > 0:
        if edad < 13:
            print("Niño")
        elif 13 <= edad <= 17:
            print("Adolescente")
        elif 18 <= edad <= 59:
            print("Adulto")
        else:
            print("Adulto mayor")
    else:
        print("Error: La edad debe ser un número entero positivo.")


# Solicita una palabra al usuario
palabra = input("Ingrese una palabra (sin espacios): ")

# Inicializa contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Recorre cada carácter en la palabra
for letra in palabra:
    if letra == 'a' or letra == 'A':
        contador_a += 1
    elif letra == 'e' or letra == 'E':
        contador_e += 1
    elif letra == 'i' or letra == 'I':
        contador_i += 1
    elif letra == 'o' or letra == 'O':
        contador_o += 1
    elif letra == 'u' or letra == 'U':
        contador_u += 1

# Muestra los resultados
print("Cantidad de 'a' o 'A':", contador_a)
print("Cantidad de 'e' o 'E':", contador_e)
print("Cantidad de 'i' o 'I':", contador_i)
print("Cantidad de 'o' o 'O':", contador_o)
print("Cantidad de 'u' o 'U':", contador_u)

# Total de vocales
total = contador_a + contador_e + contador_i + contador_o + contador_u
print("Total de vocales:", total)
