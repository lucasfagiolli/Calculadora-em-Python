import os

# Inicio do programa
lista = ["0 : Soma", "1 : Subtração", "2 : Multiplicação", "3 : Divisão", "4 : Exponenciação"]

while True :

    # Print da lista e escolha da conta.
    print("{} \n{} \n{} \n{} \n{}".format(lista[0], lista[1], lista[2], lista[3],lista[4] ))
    print("Escolha a operação que deseja realizar:")
    n = float(input())

    # Validando Soma
    if n == 0:
        print("+ escolhida.")
        print("Qual o primeiro valor?")
        n1_soma = float(input())
        print("Qual o segundo valor?")
        n2_soma = float(input())
        total_soma = n1_soma + n2_soma 
        print("{} + {} = {}".format(n1_soma, n2_soma, total_soma))



    # Validando Subtração
    elif n == 1:
        print("- escolhida.")
        print("Qual o primeiro valor?")
        n1_sub = float(input())
        print("Qual o segundo valor?")
        n2_sub = float(input())
        total_sub = n1_sub - n2_sub
        print("{} - {} = {}".format(n1_sub, n2_sub, total_sub))


    # Validando Multiplicação
    elif n == 2:
        print("x escolhida.")
        print("Qual o primeiro valor?")
        n1_multi = float(input())
        print("Qual o segundo valor?")
        n2_multi = float(input())
        total_multi = n1_multi * n2_multi
        print("{} x {} = {}".format(n1_multi, n2_multi, total_multi))



    # Validando Divisão
    elif n == 3:
        print("÷ escolhida.")
        print("Qual o primeiro valor?")
        n1_div = float(input())
        print("Qual o segundo valor?")
        n2_div = float(input())
        total_div = n1_div / n2_div
        print("{} ÷ {} = {}".format(n1_div, n2_div, total_div))    


    # Validando Exponenciação
    elif n == 4:
        print("^ escolhida.")
        print("Qual o primeiro valor?")
        n1_expo = float(input())
        print("Qual o segundo valor?")
        n2_expo = float(input())
        total_expo = n1_expo ** n2_expo
        print("{} ^ {} = {}".format(n1_expo, n2_expo, total_expo)) 


    # Condição para terminar ou continuar
    print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
    fim = input()

    if fim == str(1):
        break
    else:
        # Limpar a tela utilizando "cls" para windows se não "clear" para outro sistema Operacional
        os.system('cls' if os.name == 'nt' else 'clear') 

# fim do programa
print("...........................Fim...............................")
