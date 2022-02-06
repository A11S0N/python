import random

def jogar():
    print("*********************************")
    print("*******JOGO DE ADIVINHAÇÃO*******")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas +1):
        print("rodada {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou  ", chute_str)
        chute   = int(chute_str)

        if(chute < 1 or chute > 101):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou  e fez {} pontos!!!".format(pontos))
            break
        else:
            print("Você errou !!!")
            if(maior):
                print("Você chutou acima do número secreto")
            elif(menor):
                print("Você chutou abaixo do número secreto")
            pontos_peridos = abs(numero_secreto - chute)
            pontos = pontos - pontos_peridos
    print("***************************************")
    print("FIM DO JOGO!")
    print("***************************************")

if(__name__ == "__main__"):
    jogar()
