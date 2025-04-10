import random

print("Bem-vindo ao Jogo da Adivinhação!")
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
