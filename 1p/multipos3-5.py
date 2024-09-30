# Si enumeramos todos los números naturales a continuación 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6, y 9. La suma de estos múltiplos es 23 . Halla la suma de todos los múltiplos de 3 o 5  abajo 1000. 


def sumaMultiplos_3_5(num):
    l_num = 0
    for i in range(num):
        if (not(i % 3)  or  not(i % 5)):
            l_num += i

    return l_num

print(sumaMultiplos_3_5(1000))






