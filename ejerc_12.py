2. La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
la siguiente:
[
'-*-*-',
'--*--',
'----*',
'*----',
]
Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
anterior, sería:
[
'1*3*1',
'12*32',
'1212*',
'*1011',
]
Nota: Defina al menos una función en el código (si hay mas mejor) y documente las mismas con
docstring que es lo que hacen.

import numpy as np

filas= int(input("Ingrese el numero de filas"))
columnas= int(input("Ingrese el numero de columnas"))

valores= list(