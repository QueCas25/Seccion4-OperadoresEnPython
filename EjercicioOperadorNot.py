# Ejercicio Asistir a juego de su hijo pero con NOT
# Si no son vacaciones y tampoco es dia de descanso NO PUEDE ASISTIR

vacaciones = False
diaDescanso = False

asistencia = vacaciones or diaDescanso


if not asistencia:
# o pude usar if not(vacaciones or diaDescanso):
# Estamos invirtiendo la logica, en vez de un OR se convierte en AND
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")