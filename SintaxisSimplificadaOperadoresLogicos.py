# Simplificacion de operadores logicos

#AND

edad = int(input('Ingresa tu edad: '))

if (20 <= edad <30) or (30 <= edad < 40):
 #Simplificamos el AND, se sobre entiende que si o si tiene que
 # edad estar en ese rango

# O puede hacerse como hice yo: edad >= 20 and edad <= 30 or
# edad >= 30 and edad <= 40
# pero se pierde la sentencia del if primero ya que no hay variables
    print(f'Esta persona se encuentra en el rango de 20s y 30s')
else:
    print('Esta persona se encuentra fuera de ambos rangos')