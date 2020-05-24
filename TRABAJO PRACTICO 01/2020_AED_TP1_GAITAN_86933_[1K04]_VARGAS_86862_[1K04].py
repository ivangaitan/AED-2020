""""" TRABAJO PRACTICO 01 DE AED 2020.
El programa debe cargar por teclado los datos generales del paciente y los datos que describen los síntomas que presenta ese paciente, y en función de esos datos informar el siguiente cuadro de diagnóstico:
Si es un caso sospechoso.
Si es un caso autóctono:
Presenta al menos 2 de los síntomas respiratorios consultados.
No ha estado en contacto con casos confirmados ni tiene historial de viaje fuera del país, pero estuvo en zonas de transmisión local.
Si es un caso NO sospechoso, pero pertenece al grupo de riesgo porque el paciente es mayor a 60 años.
La carga de datos debe hacerse de forma que se evite el ingreso de datos innecesarios, descartando rápidamente los casos que no sean sospechosos a medida que los datos se van cargando. Para ello, el esquema de carga sugerido puede ser el siguiente:

1.) En primer lugar, cargar la edad,  la temperatura corporal y un valor que indique si el paciente tiene neumonía ya evidenciada. En caso de efectivamente padecer neumonía, el caso es sospechoso sin tener en cuenta las demás variables. Queda a criterio del estudiante la forma en que cargará por teclado el indicador de neumonía.
2.) Si el paciente no tiene neumonía, pero presenta fiebre (temperatura corporal mayor a 37 grados), continuar con la carga de valores que indiquen los síntomas respiratorios (tos, odinofagia o dificultad respiratoria) que se ven en la tabla del Ministerio. Al hacer la carga, tenga en cuenta que un paciente puede tener más de uno de esos síntomas a la vez, y debe cargar entonces tres indicadores: uno para tos, uno para odinofagia, y otro para dificultad respiratoria. Queda a criterio del estudiante la forma en que cargará por teclado los tres indicadores mencionados.
3.) Habiendo cargado los datos del punto 2, si hay fiebre y al menos uno de los síntomas respiratorios, cargar lo siguiente (en todos los casos, se deja para el estudiante determinar la forma en que cargará los indicadores solicitados):

Un valor que indique si el paciente es personal de salud.
Un valor que indique si estuvo en contacto con casos confirmados.
Un valor que indique si viajó al exterior.
Un valor que indique si estuvo en zonas nacionales con casos de transmisión local confirmados.
Una vez cargados los datos que correspondan, según el esquema anterior, procesar esos datos y notificar en pantalla los resultados pedidos en el cuadro de diagnóstico.
"""

__author__ = 'TP1-G130'

print('Bienvenido al Programa para Diagnóstico del COVID-19.')
# Carga de datos del paciente
edad = int(input('\nIngrese la edad del paciente: '))
tempCorp = float(input('Ingrese la temperatura corporal del paciente: '))
neumonia = int(input('En caso de que el paciente tenga NEUMONIA ya evidenciada, marque "1".\nSi el paciente no tiene NEUMONIA ya evidenciada marque "2":\n --> '))

if neumonia == 2:
    if tempCorp > 37:
        # Carga variables sintomas
        tos = int(input('En caso de que el paciente tenga TOS, marque "1". \nSi el paciente no tiene TOS marque "2":\n --> '))
        odinofagia = int(input('En caso de que el paciente tenga ODINOFAGIA, marque "1". \nSi el paciente no tiene ODINOFAGIA marque "2":\n --> '))
        difRespiratoria = int(input('En caso de que el paciente tenga Dificultad Respiratoria, marque "1".\nSi el paciente no tiene Dificultad Respiratoria marque "2":\n --> '))
        if tos == 1 or odinofagia == 1 or difRespiratoria == 1:
            perSalud = int(input('Si el paciente es Personal de Salud, marque "1".\nSi no lo es, marque "2":\n --> '))
            contactoCasoConfirmado = int(input('Si el paciente estuvo en Contacto con algun caso confirmado de COVID-19, marque "1".\nSi no lo es, marque "2":\n --> '))
            viajExt = int(input('Si el paciente tiene registro de viaje al exterior en los ultimos 14 dias, marque "1".\nSi no lo es, marque "2":\n --> '))
            transLocal = int(input('Si el paciente estuvo en zonas nacionales con casos de transmision local confirmada, marque "1".\nSi no lo es, marque "2":\n --> '))
            if (tos == 1 and odinofagia == 1 or tos == 1 and difRespiratoria == 1 or odinofagia == 1 and difRespiratoria == 1) and transLocal == 1:
                alerta = 'El paciente es un CASO AUTOCTONO.'
            else:
                alerta = 'El paciente es un CASO SOSPECHOSO de COVID-19.'
    elif edad > 60:
        alerta = 'CASO RIESGOSO, paciente mayor a 60 años.'
    elif edad <= 60:
        alerta = 'Paciente No sospechoso'
elif neumonia == 1:
    alerta = 'El paciente es un CASO SOSPECHOSO de COVID-19.'
else:
    print('Por favor, Ingrese una opcion valida.')


print('Resultado de diagnostico: ', alerta)






















