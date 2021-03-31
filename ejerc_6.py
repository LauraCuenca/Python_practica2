frase="""
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
minuscula= frase.lower().split(' ')

quitar= ",;:.\n!\"'"

for caracter in quitar:
    frase= frase.replace(caracter,
    
                                "")

frase= frase.lower()

minuscula= frase.split(' ')

dicc_frecuencias = {}
for palabra in minuscula:
    if palabra in dicc_frecuencias:
        dicc_frecuencias[palabra] += 1
    else:
        dicc_frecuencias[palabra] = 1

print(dicc_frecuencias.keys())


