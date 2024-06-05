# Tienda de libros
# Proporciona nombre de libro, id de libro, precio en flotante, y envio gratuito con booleanos
# desplegar la info del libro

nombreLibro = str(input('Ingresa el nombre del libro: '))
idLibro= int(input('Ingresa el id del libro: '))
precioLibro = float(input('Ingresa el precio del libro: '))
envioGratisLibro = bool(input('El libro tiene envio gratis? (Si/No): '))
#Este input cualquier cosa diferente de vacio lo regresa como TRUE
# Si lo dejo en blanco lo deja como false
#tenemos que hacer una comprobacion o validacion

if envioGratisLibro == 'Si': #se pueden poner cadenas directo para comprobar
    envioGratisLibro = True
else:
    if envioGratisLibro == 'No':
        envioGratisLibro = False
    else:
        print('Valor incorrecto, escriba Si o No')

print(f'Nombre: {nombreLibro}')
print(f'Id: {idLibro}')
print(f'Precio: {precioLibro}')
print(f'Envio gratuito?: {envioGratisLibro}')
