# Calcular la Cantidad Mínima de Monedas para el Cambio de una Compra


def calcular_cantidad_menor_de_monedas(ingreso):
    monedas = [500, 300, 100, 50, 20, 10]

    cantidad_monedas = 0
    for i in range(len(monedas)):

        moneda = monedas[i] # valor de la moneda
        cantidad_monedas += int(ingreso / moneda) # Catidad de monedas para el valor
        ingreso = int(ingreso % moneda) # actulizar ingreso

    return cantidad_monedas


print(calcular_cantidad_menor_de_monedas(1000))
print(calcular_cantidad_menor_de_monedas(10531))
print(calcular_cantidad_menor_de_monedas(100093))


