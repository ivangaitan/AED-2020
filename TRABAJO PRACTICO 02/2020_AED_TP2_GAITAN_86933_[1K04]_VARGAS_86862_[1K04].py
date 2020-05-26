import random

# pide ingresar un usuario
cuenta_usuario  = str(input("Ingrese su usuario: ")).capitalize()
arroba = cuenta_usuario.count("@")
intentos = 0

# verifica que el usuario sea valido y si es invalido da 3 intentos
while '..' in cuenta_usuario or cuenta_usuario.startswith(".") == True or cuenta_usuario.endswith(".") == True or arroba > 1 or arroba == 0 or cuenta_usuario.startswith("@") == True or cuenta_usuario.endswith("@") == True or not cuenta_usuario:
    intentos += 1
    if intentos == 3:
        print ("Demasiados intentos")
        break;
    cuenta_usuario = str(input("El usuario ingresado es incorrecto, ingrese nuevamente el usuario: "))
    arroba = cuenta_usuario.count("@")

# pide al usuario la cantidad de pacientes a analizar
cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a procesar: "))
paciente = [1]

# definimos los datos de cada paciente que necesita el usuario
resultado_test = ["Test Positivo", "Test Negativo"]
region = ["Capital", "Gran Cordoba", "Norte", "Sur"]
contacto_casos_confirmados = ["Tuvo contacto con casos confirmados", "No tuvo contacto con casos confirmados"]
personal_salud = ["Es personal de salud", "No es personal de salud"]
viajo_exterior = ["Viajo al exterior", "No viajo al exterior"]

# agrega la cantidad de pacientes a la lista paciente
for p in paciente:
    p += 1
    paciente.extend([p])
    if p == cantidad_pacientes:
        break;

# a cada paciente le crea datos aleatorios y los agrega a una lista
for i in paciente:
    edad = random.randint(2, 100)
    i = ["paciente: " + str(paciente.index(i) + 1), str(edad) + " años", random.choice(resultado_test), "Region: " + random.choice(region), random.choice(contacto_casos_confirmados), random.choice(personal_salud), random.choice(viajo_exterior)]
    print(i)







