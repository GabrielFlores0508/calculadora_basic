# Projeto calculadora

import math

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def calculadora():

    resultado = 0

    while True:
        escolha = input("Digite sua opção: ")
        if escolha not in ["1", "2", "3", "4", "88", "99"]:
            print("Escolha uma opção válida!\n")
        else:
            if escolha == "99":
                break

            if escolha == "88":
                resultado = 0
            else:
                try:
                    if resultado == 0: 
                        n1 = float(input("Digite o primeiro número: "))
                        n2 = float(input("Digite o segundo número: "))
                    else:
                        n1 = resultado
                        n2 = float(input("Digite um número: "))

                    print("")

                    if escolha == "1": 
                        resultado = soma(n1, n2)
                    elif escolha == "2":
                        resultado = subtracao(n1, n2)
                    elif escolha == "3":
                        resultado = multiplicacao(n1, n2)
                    elif escolha == "4":
                        if n2 != 0: 
                            resultado = divisao(n1, n2)
                        else:
                            print("Erro: Impossível dividir por 0 (zero)\n") 

                    print(resultado)
                except ValueError:
                    print("Digite apenas números.")
                except Exception:
                    print("Erro inesperado.")

print("Bem vindo a minha calculadora!\n")

print("Selecione a operação:")
print("1 = para adição")
print("2 = para subtração")
print("3 = para multiplicação")
print("4 = para divisão")
print("88 = para zerar\n")
print("99 = sair\n")

try:
    calculadora()
except Exception:
    print("Erro geral inesperado.")