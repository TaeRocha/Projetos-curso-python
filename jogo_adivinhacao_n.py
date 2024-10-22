"""
Desenvolver um jogo de adivinhação de números.
Criar funções para operações matemáticas básicas e usar em um script.
"""
import random

print("Bem vido ao jogo de adivinhação. ")

print(
    """
    As regras do jogo são simples: 

    1. Você recebe um número aleatório entre 1 e 9 que será usado
    para multiplicar um número, também de 1 a 9, que é o correto
    2. A cada nova tentativa, você recebe um multiplicador diferente
    que você não vai saber, apenas a multiplicação resultante
    3. Se tiver abaixo ou acima do número, recebe uma mensagem sobre

    O seu trabalho é tentar adivinhar o número levando em conta que ele
    estará multiplicado por um número aletório a cada nova chance. 

    Boa sorte! 
    """
)

def adivinhacao():
    numero_correto = random.randint(1, 9)
    return numero_correto
    
# def multiplicacao():
#     multiplicador = range(1, 10)
#     return multiplicador
# Ele estava retornando o interável range, que seria o intervalo 
    # que o range pode gerar, mas não um dos número em si. 

def multiplicacao():
    numero_multiplicador = random.randint(1, 9)
    return numero_multiplicador 
        
numero = int(input("Primeiro, digite um número para começarmos: "))
numero_correto = adivinhacao()
condicao = True

while condicao:
    condicao = numero != numero_correto

    numero_multiplicado = numero_correto * multiplicacao()
    print(f"Seu número é {numero_multiplicado}, agora tente adivinhar")
    numero = int(input("Digite o novo número: "))

    if numero == numero_correto:
        print(f"Parabens! O número é o {numero} mesmo")
        break
    elif numero > numero_correto:
        print(f"O número {numero} é maior que o número correto")
        continue
    elif numero < numero_correto:
        print(f"O número {numero} é menor que o número correto")
        continue