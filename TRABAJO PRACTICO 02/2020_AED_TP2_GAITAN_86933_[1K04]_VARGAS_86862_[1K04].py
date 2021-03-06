import random

cuenta_usuario = str(input("Ingrese su usuario: ")).capitalize()
arroba = 0
intentos = 0

for a in cuenta_usuario:
    if a == '@':
        arroba+= 1

# Validar cuenta...
while '..' in cuenta_usuario or not cuenta_usuario or cuenta_usuario[0] == '.' or cuenta_usuario[-1] == '.' or arroba > 1 or arroba == 0 or cuenta_usuario[-1] == '@' or  cuenta_usuario[0] == '@':
    intentos += 1
    if intentos == 3:
        print("Demasiados intentos")
        break
    cuenta_usuario = str(input("El usuario ingresado es incorrecto, ingrese nuevamente el usuario: "))
    arroba = cuenta_usuario.count("@")

# Crear funciones

def cantConfirmados(a):
    if a == 'Positivo':
        return True
    return False

def porcentaje(b, c):
    por = (c * 100) / b
    return por


def promedio(a, b):
    if b == 0:
        return a
    prom = a / b
    return prom


# Solicitar al usuario que ingrese la cantidad de pacientes a procesar...
n = int(input('Ingrese la cantidad de pacientes que desea procesar: '))
test = ('Positivo', 'Negativo')
regiones = ('Capital', 'Gran Córdoba', 'Norte', 'Sur')
viajExt = perSalud = contactoCaso = ('Si', 'No')

# Definir variables a utilizar..
confirmados = porcentajeConf = acEdad = contEdad = cantPer = acEdad1 = autoc = cantViaje = contaConfir = 0
menor = None
regioncapital = regionGC = regionNorte = regionSur = 0

# Por cada paciente sospechoso, generar de manera aleatoria
for i in range(n):
    edad = random.randint(16, 99)
    resulTest = random.choice(test)
    regionPac = random.choice(regiones)
    contactoCasoCon = random.choice(contactoCaso)
    personalSalud = random.choice(perSalud)
    ViajeExt = random.choice(viajExt)
    print(edad, resulTest, regionPac, contactoCasoCon, personalSalud, ViajeExt)

    # Caso autoctono
    if resulTest == 'Positivo' and contactoCasoCon == 'No' and personalSalud == 'No' and ViajeExt == 'No':
        autoc += 1
        # 5. Menor edad entre los casos autóctonos.
        if i == 0 or edad < menor:
            menor = edad

    # 1. Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.
    if cantConfirmados(resulTest):
        confirmados += 1

    # 2. Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el test debe ser negativo y tener más de 60 años).
    if resulTest == 'Negativo' and edad > 60:
        contEdad += 1
        acEdad += edad

    # 3. Cantidad y porcentaje que el personal de salud representa sobre el total de casos.
    if personalSalud == 'Si':
        cantPer += 1

    # 4. Edad promedio entre los casos confirmados.
    acEdad1 += edad

    # 6. Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.
    if resulTest == 'Positivo' and regionPac == 'Capital':
        regioncapital += 1
    elif resulTest == 'Positivo' and regionPac == 'Gran Córdoba':
        regionGC += 1
    elif resulTest == 'Positivo' and regionPac == 'Norte':
        regionNorte += 1
    elif resulTest == 'Positivo' and regionPac == 'Sur':
        regionSur += 1

    # 7. Cantidad de casos confirmados con viaje al exterior.
    if resulTest == 'Positivo' and ViajeExt == 'Si':
        cantViaje += 1

    # 8. Cantidad de casos sospechosos en contacto con casos confirmados.
    if contactoCasoCon == 'Si':
        contaConfir += 1

    # 9. Las regiones sin casos confirmados.
    if resulTest == 'Negativo':
        pass


# 1
porcentajeConf = porcentaje(n, confirmados)
# 2
PromEdad = promedio(acEdad, contEdad)
# 3
porcentajePer = porcentaje(n, cantPer)
# 4
promEdad1 = promedio(acEdad1, n)
# 6
porcentajeCapital = porcentaje(n, regioncapital)
porcentajeGC = porcentaje(n, regionGC)
porcentajeNorte = porcentaje(n, regionNorte)
porcentajeSur = porcentaje(n, regionSur)

print('\nCantidad de confirmados: ', confirmados, 'y el porcentaje sobre el total de casos: ', porcentajeConf, '%')
print('\nEdad promedio de los pacientes que pertenecen a grupo de riesgo: ', PromEdad)
print('\nLa cantidad de sospechosos que forman parte del personal de salud son', cantPer, 'los cuales representan un ', porcentajePer, '%')
print('\nEdad promedio entre los casos confirmados: ', promEdad1)
print('\nMenor edad entre los casos autoctonos: ', menor, 'cantidad de casos: ', autoc)
print('\nCantidad de casos confirmados por region: \nRegion Capital:', regioncapital, 'los cuales representan un', porcentajeCapital, '% sobre el total de casos.\nRegion Gran Cordoba:', regionGC, 'los cuales representan un', porcentajeGC, '% sobre el total de los casos.\nRegion Norte:', regionNorte, 'los cuales representan un', porcentajeNorte, '% sobre el total de los casos.\nRegion Sur:', regionSur, 'los cuales representan un', porcentajeSur, '% sobre el total de los casos.')
print('\nCantidad de confirmados con viaje al exterior:')
print('\nCantidad de confirmados con viaje al exterior:', cantViaje)
print('\nCantidad de casos sospechosos en contacto con casos confirmados:', contaConfir)
