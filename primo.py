# Desafio 1
# Escreva uma função em Python para encontrar os fatores primos que compõem um número
def funcfatoresprimos (valorpassado):
    numeropassado = valorpassado
    divisor = 2
    fatoresprimos = []

    while numeropassado != 1:
        resto = numeropassado % divisor
        if resto == 0:
            fatoresprimos.append(divisor)
            numeropassado = numeropassado/divisor
        else:
            divisor += 1
    return fatoresprimos

numerooriginal = input('Digital o número que deseja receber os fatores primos: ')
resultado = funcfatoresprimos(int(numerooriginal))
print ('Número Passado: ' + str(numerooriginal))
print ('Fatores Primos: ' + str(resultado))
