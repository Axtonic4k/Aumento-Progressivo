# Importando o módulo time para lidar com operações relacionadas ao tempo
import time


# Definindo a função adicionar_porcentagem que recebe um número x e retorna o valor de x aumentado em 20%
def adicionar_porcentagem(x):
    return x + (x * 0.2)


# Solicitando ao usuário que digite um número e armazenando-o na variável x após convertê-lo para um float
x = float(input("Digite um número: "))

# Definindo o número de iterações para o loop
iterações = 16

# Definindo a duração do intervalo de espera entre iterações em segundos
tempo = 1

# Loop que executa o código 16 vezes
for i in range(iterações):
    # Chamando a função adicionar_porcentagem para atualizar o valor de x e armazenando o novo valor em x
    x = adicionar_porcentagem(x)

    # Imprimindo o número da iteração e o valor atualizado de x
    print("Iteração:", i + 1, " - Valor de x:", x)

    # Pausando a execução do programa pelo tempo definido
    time.sleep(tempo)
