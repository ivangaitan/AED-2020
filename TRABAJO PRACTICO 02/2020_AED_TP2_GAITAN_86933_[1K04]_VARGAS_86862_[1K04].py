cuenta_usuario  = str(input("Ingrese su usuario: ")).capitalize()
arroba = cuenta_usuario.count("@")
intentos = 0

while '..' in cuenta_usuario or cuenta_usuario.startswith(".") == True or cuenta_usuario.endswith(".") == True or arroba > 1 or arroba == 0 or cuenta_usuario.startswith("@") == True or cuenta_usuario.endswith("@") == True or not cuenta_usuario:
    intentos += 1
    if intentos == 3:
        print ("Demasiados intentos")
        break;
    cuenta_usuario = str(input("El usuario ingresado es incorrecto, ingrese nuevamente el usuario: "))
    arroba = cuenta_usuario.count("@")





