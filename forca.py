import random

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "computador", "algoritmo"]
    return random.choice(palavras)

def exibir_forca(erros):
    forca = [
        '''
          +---+
              |
              |
              |
             ===''',
        '''
          +---+
          O   |
              |
              |
             ===''',
        '''
          +---+
          O   |
          |   |
              |
             ===''',
        '''
          +---+
          O   |
         /|   |
              |
             ===''',
        '''
          +---+
          O   |
         /|\  |
              |
             ===''',
        '''
          +---+
          O   |
         /|\  |
         /    |
             ===''',
        '''
          +---+
          O   |
         /|\  |
         / \  |
             ==='''
    ]
    print(forca[erros])

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == "s"

def jogar_forca():
    while True:
        palavra = escolher_palavra()
        letras_certas = []
        letras_erradas = []
        vidas = 5

        print("Bem-vindo ao jogo da forca!")
        print("Adivinhe a palavra secreta digitando letras.")
        
        while vidas > 0:
            for letra in palavra:
                if letra in letras_certas:
                    print(letra, end=" ")
                else:
                    print("_", end=" ")
            
            print("\n")
            exibir_forca(len(letras_erradas))
            print("Vidas restantes:", vidas)
            print("Letras erradas:", letras_erradas)

            chute = input("Digite uma letra: ").lower()

            if chute in letras_certas or chute in letras_erradas:
                print("Você já tentou essa letra antes. Tente novamente.")
                continue

            if chute in palavra:
                letras_certas.append(chute)
                
                if len(letras_certas) == len(set(palavra)):
                    print("Parabéns! Você ganhou!")
                    print("A palavra era:", palavra)
                    break

            else:
                letras_erradas.append(chute)
                vidas -= 1

        if vidas == 0:
            print("Você perdeu!")
            print("A palavra era:", palavra)
            print("Letras erradas:", letras_erradas)

        if not jogar_novamente():
            break

jogar_forca()
