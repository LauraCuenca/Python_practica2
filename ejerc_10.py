def calcular_valor(car):
    cant= 0
    if car in ('A, E, I, O, U, L, N, R, S, T'):
        cant+= 1
    elif car in (' D, G') :
        cant+= 2
    elif car in  ('B, C, M, P'):
        cant+= 3
    elif car in ('F, H, V, W, Y'):
        cant += 4
    elif car in ('K'):
        cant+= 5
    elif car in ('J, X'):
        cant+= 8
    else:
        cant+= 10
    return cant


palabra= input('Ingrese una palara, para saber su valor: ').upper()

cant_total= 0
for car in palabra:
    cant_total+=(calcular_valor(car))
print("valor: "+repr(cant_total))