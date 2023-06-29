import random

def jogar_jogo():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    while tentativas < 10:
        tentativas += 1
        palpite = int(input("Digite um número: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número!")
            jogar_novamente()
            return

        elif palpite < numero_secreto:
            print("Você errou! O número correto é maior.")

        else:
            print("Você errou! O número correto é menor.")

    print("Suas tentativas acabaram! O número correto era", numero_secreto)
    jogar_novamente()

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    if resposta.lower() == "s":
        jogar_jogo()
    else:
        print("Obrigado por jogar!")

jogar_jogo()
