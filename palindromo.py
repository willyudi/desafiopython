# Desafio 2
# Escreva uma função em Python que determina se um determinado texto é palíndromo
# Palíndromo é uma palavra ou frase que pode ser lida da esquerda para a direita e vice-versa
# Exemplo: Arara ou a frase O céu sueco
# Entrada: Uma string de tamanho qualquer
# Saída: Um valor boleano (True ou False)
# A função só deve considerar letras (a-z)
# Deve ignorar acentos
# Deve ignorar a captalização
def funcpalindromo (palavrapassada):
    from unicodedata import normalize

    palavratratada = palavrapassada.lower()
    palavratratada = palavratratada.replace(" ", "")
    palavratratada = normalize('NFKD', palavratratada).encode('ASCII', 'ignore').decode('ASCII')
    tamanho = len(palavratratada)
    novapalavra = ''
    for x in range(tamanho):
        novapalavra = novapalavra + palavratratada[int(tamanho)-(x+1)]

    if novapalavra == palavratratada:
        return True
    else:
        return False

palavra = input('Passar a palavra ou frase: ')
if funcpalindromo(palavra):
    print('É Palíndromo')
else:
    print('Não é Palíndromo')
    