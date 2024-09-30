# Encontrar la Cantidad de Potencias de 2 a la n en una Cadena de Caracteres 


# "24816" -> 2 4 8 16 -> 4 potencias de 2
# "8162" -> 3 pontencias de 2

def potencia2(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return potencia2(n//2)

def cantPotencias2(str_):
    n = len(str_)

    numeros_enco = list()
    for i in range(n):
        strn = ""
        for j in range(n - i):
            strn = strn + str_[i+j]
            numeros_enco.append(int(strn))
            #print(f"i: {i} j: {j}: -> {strn}")

    n_num = 0
    for i in numeros_enco:
        if (potencia2(i)):
            n_num += 1

    return n_num


l = cantPotencias2("248")
print(l)











