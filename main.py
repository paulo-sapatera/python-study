nome = "Angelina Jolie"
print(nome[0:8])
print(nome.split())
print(nome.split()[1])

""" 1 faca com que um programa leia um numero inteiro e imprima-o
    2 faca um programa que peca ao usuario digitar 3 valores inteiros e imprima a soma deles
    3 faca um programa que receba 3 valores e apresente a soma dos quadrados dos valores lidos
""" 
#1
intnumber = 1
print(intnumber)

#2
num1 = (int(input("Digite um numero inteiro:")))
num2 = (int(input("Digite um numero inteiro:")))
num3 = (int(input("Digite um numero inteiro:")))

print(num1,num2,num3)

soma = (num1+num2+num3)
print(soma)

#3
nums = [3,6,12] #number list
print(nums)
num1 = nums[0]**2
num2 = nums[1]**2
num3 = nums[2]**2

soma = num1+num2+num3

print("A soma dos quadrados eh:", soma)

################################################################


