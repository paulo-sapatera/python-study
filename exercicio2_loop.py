"""
Faca um programa que utilize o comando while para mostrar na tela uma contagem regressiva, inciando em 10 e terminando em 0.
Mostre tambem uma mensagem "FIM!" apos a contagem.
"""

num = 10

while num >= 0:
    print(num)
    num = num -1
    if num == 0:
        print("FIM!")