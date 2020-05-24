cuenta_usuario = str(input("Ingrese su usuario: ")).capitalize()

start =  cuenta_usuario.startswith(".")
end =  cuenta_usuario.endswith(".")
arroba = cuenta_usuario.count("@")
inicia_arroba = cuenta_usuario.startswith("@")
finaliza_arroba = cuenta_usuario.endswith("@")
posicion_ultimo_caracter = len(cuenta_usuario) - 1

if '..' in cuenta_usuario or start == True or end == True or arroba > 1 or inicia_arroba == True or finaliza_arroba == True:
    cuenta_usuario = False

print (cuenta_usuario)