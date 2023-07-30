menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[l] Alterar Limite de Saque
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
mumero_saques = 0
LIMITE_SAQUES = 3

def parse_input(parsing_function):
    value = 0
    try:
        value = parsing_function(input())
    except:
        print("Valor inválido. Por favor, utilize apenas números e '.'.")
    else:
        return value
    finally:
        return value if value != 0 else 0


def print_no_newline(string):
    print(string, end='')
    

while True:

    opcao = input(menu)
    match opcao:
        case "d":
            print("Depósito")
            print_no_newline("Digite o valor a ser depositado: R$")
            deposito = parse_input(float)
            saldo += deposito
            print(f'Saldo: R${saldo:.2f}')
            extrato += f'Depósito: R${deposito:.2f}\n'
        case "s":
            print("Saque")
            print_no_newline(f'Digite o valor a ser sacado, observando o limite de R${limite:.2f} por saque: R$')
            saque = parse_input(float)
            if (saque > limite):
                print_no_newline("Valor acima do limite permitido. Tente novamente com um valor menor que o limite atual.")
            elif (saque > saldo):
                print_no_newline(f'Saldo insuficiente. Saldo atual: R${saldo:.2f}')
            elif (LIMITE_SAQUES <= 0):
                prinf("Limite de saques atingido")
            else:
                print(f'Saque realizado. Valor: R${saque:.2f}')
                extrato += f'Saque: R${saque:.2f}\n'
                saldo -= saque
                print(f'Saldo atual: R${saldo:.2f}')
                LIMITE_SAQUES -= 1
        case "e":
            print("Extrato\n")
            print(extrato, '\n')
            print_no_newline(f'Saldo atual: R${saldo:.2f}\nLimite de Saque atual: R${limite}')
        case "l":
            print(f'Alterar limite de saque. Limite atual: R${limite:.2f}')
            print_no_newline("Digite o novo valor desejado: R$")
            limite = parse_input(int)
            print_no_newline(f'Novo limite para saques: R${limite:.2f}')
            extrato += f'Alteração de limite: R${limite:.2f}\n'
        case "q":
            break
        case _:
            print_no_newline("Operação inválida, por favor selecione novamente a operação desjada.")
