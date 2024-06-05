#Como saber si una edad se encuentra entre los 20 y 30

edad = int(input('Ingresa tu edad: '))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if veintes or treintas:
# O puede hacerse como hice yo: edad >= 20 and edad <= 30 or
# edad >= 30 and edad <= 40
# pero se pierde la sentencia del if primero ya que no hay variables
    print(f'Esta persona se encuentra en el rango de 20s y 30s')
    if veintes:
        print('Esta persona se encuentra en sus veintes')
    elif treintas:
        print('Esta persona se encuentra en sus treintas')
else:
    print('Esta persona se encuentra fuera de ambos rangos')