#Edad de una persona
#Adulta >=18

edadAdulto = 18
edadPersona = int(input('Ingresa tu edad: '))

if edadPersona >= edadAdulto:
    print(f'La edad de {edadPersona} es de un adulto')
else:
    print(f'La edad de {edadPersona} es la edad de un menor de edad')
