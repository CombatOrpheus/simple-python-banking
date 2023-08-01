from typing import List, Callable
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
limite_saques = 3

def parse_input(parsing_function: Callable[[any], str]):
    value = 0
    try:
        value = parsing_function(input("Digite o valor da operação: R$"))
    except:
        print("Valor inválido. Por favor, utilize apenas números e '.'.")
    else:
        return value
    finally:
        return value if value != 0 else 0


def deposito(saldo: float, valor: float, extrato: List[str]) -> (float, str):
    saldo += valor
    mensagem = f'Depósito: R${valor:.2f}\n'
    extrato += mensagem
    print(mensagem)
    return (saldo, extrato)


def saque(saldo: float, valor: float, limite_operacao: int, extrato: List[str], *, limite_saques: int = limite_saques) -> (float, str, int):
    if saldo < valor:
        print("Saldo insuficiente")
        return (saldo, valor, limite)
    elif valor > limite:
        print("Limite excede o permitido para esta operação")
        return (saldo, valor, limite)
    else:
        mensagem = f'Saque: R${valor:.2f}\n'
        extrato += mensagem
        print(mensagem)
        saldo -= valor 
        print(f'Saldo atual: R${saldo:.2f}')
        return (saldo, extrato, limite_saques - 1)


def exibir_extrato(extrato: List[str]):
    mensagem = '=' * 10 + "Extrato" + '=' * 10 + '\n'
    print(mensagem)
    print(extrato)
    print('=' * len(mensagem))


def alterar_limite(valor: int, extrato: str) -> (int, str):
    limite = valor
    mensagem = f'Alteração de limite. Novo valor: R${valor:.2f}'
    extrato += mensagem
    print(mensagem)
    return (limite, extrato)

def adicionar_limite_saques(limite_saques: int, adicionar: int) -> int:
    return limite_saques + adicionar


while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = parse_input(float)
            saldo, extrato = deposito(saldo, valor, extrato)
        case "s":
            print(f'Limite para saques: R${limite:.2f}')
            valor = parse_input(int)
            saldo, extrato, limite_saques = saque(saldo, valor, limite, extrato, limite_saques = limite_saques)
        case "e":
            exibir_extrato(extrato)
        case "l":
            valor = parse_input(int)
            limite, extrato = alterar_limite(valor, extrato)
        case "ls":
            valor = parse_input(int)
            limite_saques = adicionar_limite_saques(limite_saques, valor)
        case "q":
            print("Finalizando programa.")
            break
        case _:
            print_no_newline("Operação inválida, por favor selecione novamente a operação desjada.")
