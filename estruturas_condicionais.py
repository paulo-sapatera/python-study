#Exercícios
""" 1 faca um programa que receba dois numeros inteiros e mostre qual deles eh o maior

    2 faca um programa que leia um numero inteiro fornecido pelo usuario, se esse numero for positivo
      calcule a raiz quadrada do numero e apresente-o, se o numero for negativo, mostre uma mensagem dizendo
      que o numero é invalido
    
    3 faca um programa que recebe um numero inteiro e informe se esse numero é par ou impar
"""

import math

#1 
num1: int = int(input("Digite o primeiro número:"))
num2: int = int(input("Digite o primeiro número:"))

if num1 > num2:
    print(f"O numero {num1} e maior que o {num2}")
else:
    print(f"O numero {num2} e maior que o {num1}")

#################################################################################################################

#2
numero: int = int(input("Digite um numero inteiro:"))

if numero > 0:
    numero = math.sqrt(numero)
    print(numero)
else:
    print(f"O numero {numero} eh negativo, portanto invalido.")

#################################################################################################################

#3
numero_inteiro: int = int(input("Digite um numero inteiro:"))

if numero_inteiro % 2 == 0:
    print(f"O numero {numero_inteiro} eh par")
else:
    print(f"O numero {numero_inteiro} eh impar") 