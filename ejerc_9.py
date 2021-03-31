palabra = input('Palabra o frase: ').replace(" ","")
letras = {}
for car in palabra:   
   if car in letras:
      letras[car] += 1
   else:
      letras[car] = 1
print(letras)

cant= 0
for car in palabra:
   if letras[car] == 1:
      cant+= 1

if cant == (len(palabra)):
   print('heterograma')
else:
   print('no heterograma')
