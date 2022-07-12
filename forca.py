
secreto = input('Escreva a palavra secreta: ').lower()
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

    if secreto_temporario == secreto:
        print('Parabéns!! você acertou a palavra secreta!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chance -= 1
    print(f'Você ainda tem {chance} chances!')