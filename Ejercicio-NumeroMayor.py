#Instrucciones

# Solicitar al usuario dos valores y determinar cual es mayor
# Se ebde imprimir el maor de los numeros
# la salida debe de ser : El numero masyor es : numero mayor

numero1 = int(input("Inserta el primer numero: "))
numero2 = int(input("Inserta el segundo numero: "))

if numero1 < numero2:
    print(f'El numero mayor es: {numero2}')
else:
    if numero1 > numero2:
        print(f'El numero mayor es: {numero1}')
    else:
        print('Los numeros son iguales')