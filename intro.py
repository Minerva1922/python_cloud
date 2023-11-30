def verificar_edad():
    
    año_nacimiento = int(input("tu año de nacimiento:1983 "))

    edad = 2023 - año_nacimiento

    
    if edad < 18 or año_nacimiento > 2023:
        print("Lo siento, no puedes entrar.")
        return

    
    print("¡Bienvenido!")

verificar_edad()
