archivo = open('numpy_readme.txt', 'r')
print ('Imprimir las lineas que contienen "http" o "https" ')
print (" ")
for linea in archivo.readlines():
    if 'http' in linea or 'https' in linea:
         print (linea)
archivo.close() 