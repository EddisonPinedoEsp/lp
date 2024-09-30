# Largest Prime Factor
# Los factores primos de 13195 son 5, 7, 13 y 29. Cuál es el mayor factor primo del número 600851475143?


def PrimeFactor(num): 
    
    primos = []
    l = True
    while(l):

        for i in range(2, int(num)+1):
            if (num % i == 0):
                primos.append(i)
                num /= i
                # print(f"n: {num} | {i}")
                break   
        # print(primos)
        # print(num)
        if (num <= 2):
            l = False


    return primos



# print(PrimeFactor(13195))
# print(max(PrimeFactor(13195)))

print(PrimeFactor(600851475143))
print(max(PrimeFactor(600851475143)))




