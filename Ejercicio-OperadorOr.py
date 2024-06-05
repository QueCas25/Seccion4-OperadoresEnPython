# Ejercicio Asistir a juego de su hijo
# Si es vacaciones o dia de descanso si puede asistir

vacaciones = False
diaDescanso = True

asistencia = vacaciones or diaDescanso


if asistencia:
# o pude usar if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")