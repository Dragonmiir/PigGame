import random

# Cóigo para definir função de rolagem


def rolagem():
    # Código usado para mais tarde ser usado quando a função for chamada
    valor_minimo = 1
    valor_maximo = 6
    rolagem = random.randint(valor_minimo, valor_maximo)

    return rolagem


# Código para definir o número de jogadores e verificar se o número de jogadores está de acordo com o limite
while True:
    jogadores = input("Ensira o numero de jogadores (2 - 4): ")
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print("Deve ser entre 2 a 4 jogadores.")
    else:
        print("Número de jogadores invalido, tente novamente.")

# Código para inciar o jogo e rolar os dados
pontuacao_maxima = 50
pontuacao_jogadores = [0 for _ in range(jogadores)]

while max(pontuacao_jogadores) < pontuacao_maxima:
    for jogadores_idx in range(jogadores):
        print("\nNumero do jogador", jogadores_idx + 1, "O turno começou!\n")
        print("Sua pontuação atual é:",
              pontuacao_jogadores[jogadores_idx], "\n")
        pontuacao_atual = 0

        while True:
            deve_rolar = input("Você gostaria de rolar (y)? ")
            if deve_rolar.lower() != "y":
                break
# Código abaixo para mencionar os valores rolados e encerrar o turno caso o valor 1 seja rolado
            valor = rolagem()
            if valor == 1:
                print("Você rolou um 1! Seu turno acabou.")
                pontuacao_atual = 0
                break
            else:
                pontuacao_atual += valor
                print("você rolou um:", valor)

            print("A sua pontuação foi de:", pontuacao_atual)

        pontuacao_jogadores[jogadores_idx] += pontuacao_atual
        print("A sua pontuação total foi de:",
              pontuacao_jogadores[jogadores_idx])

# Código para definir o ganhador com a pontuação mais alta
pontuacao_maxima = max(pontuacao_jogadores)
ganhador_idx = pontuacao_jogadores.index(pontuacao_maxima)
print("Número do jogador", ganhador_idx + 1,
      "É o ganhador! Com uma pontuação de:", pontuacao_maxima)
