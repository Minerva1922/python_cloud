def verificar_edad():
    
    año_nacimiento = int(input("tu año de nacimiento:1983 "))

    edad = 2023 - año_nacimiento

    
    if edad < 18 or año_nacimiento > 2023:
        print("Lo siento, no puedes entrar.")
        return

    
    print("¡Bienvenido!")

verificar_edad()

'''
Definir una función llamada verificar_edad. Las funciones en Python se definen con la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener parámetros (en este caso, la función no toma ningún parámetro).
año_nacimiento = int(input("Ingresa tu año de nacimiento: "))

Pide al usuario que ingrese su año de nacimiento mediante la función input. La entrada del usuario se almacena en la variable año_nacimiento, y intse utiliza para convertir la entrada a un número entero.
edad = 2023 - año_nacimiento

Calcula la edad actual restando el año de nacimiento del año actual (2023 en este caso).
if edad < 18 or año_nacimiento > 2023:

Comprueba dos condiciones: si la edad es menor de 18 o si el año de nacimiento es mayor que el año actual (2023).
print("Lo siento, no puedes entrar.")

Imprime un mensaje indicando que el usuario no cumple con las condiciones para entrar.
return

Termina la ejecución de la función en este punto. Si la condición anterior se cumple, el programa imprimirá el mensaje y saldrá de la función, impidiendo que llegue al siguiente bloque de código.
print("¡Bienvenido!")

Este mensaje solo se imprimirá si la condición en el ifno se cumple, es decir, si el usuario es mayor de 18 años y proporcionará un año de nacimiento válido.
Finalmente, la última línea verificar_edad()llama a la función, lo que inicia la ejecución del programa. El flujo del programa dependerá de las respuestas del usuario y de si cumplen con las condiciones establecidas.
'''
