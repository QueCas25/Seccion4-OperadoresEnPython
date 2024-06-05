#EjercicioValorDentroDelRango

valor = int(input(f'Escribe el valor: '))

valorMin = 0
valorMax = 5
#puede hacerse asi o con el if
#rango = valor>= valorMin and valor <=valorMax

if valor >= valorMin and valor <= valorMax:
    print(f'El valor {valor} se encuentra dentro del rango')
else:
    print(f'El valor {valor} se encuentra fuera del rango')
