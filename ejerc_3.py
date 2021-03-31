import string

def ingreso_letra():
     letra= input('Ingrese una letra para comparar ')
     while letra not in string.ascii_letters:
        print('No se a ingresado una letra ')
        letra = input('Ingrese una letra para comparar ')
     return letra


texto= """Las listas también se pueden crear usando el constructor de la clase, list(iterable). 
En este caso, el constructor crea una lista cuyos elementos son los mismos y están en el mismo orden que los ítems del iterable.
El objeto iterable puede ser o una secuencia, un contenedor que soporte la iteración o un objeto iterador."""

texto= texto.split(' ')
letra= ingreso_letra()

for palabra in texto:
    if letra == palabra[0]:
        print (palabra)
    



