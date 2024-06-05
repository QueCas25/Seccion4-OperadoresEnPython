# Ejercicio de Triangulo
# Calcular el area y perimetro de un rectangulo con las sig. variables
# alto (int)
# ancho (int)
# Usuario proporciona alto y ancho
# y se imprime
# Area= alto*ancho
# Perimetro = (alto+ancho) *2

alto = int(input('Ingrese el alto del rectangulo: '))
ancho = int(input('Inserte el ancho del rectangulo: '))

print(f'Alto: {alto}')
print(f'Ancho: {ancho}')

Area = int(alto * ancho)
Perimetro = int((alto + ancho) * 2)

print(f'El area del rectangulo es: {Area}')
print(f'El perimetro del rectangulo es: {Perimetro}')
