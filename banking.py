menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
mumero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    match opcao:
        case "d":
            print("Depósito")
        case "s":
            print("Saque")
        case "e":
            print("Extrato")
        case "q":
            break
        case _:
            print("Operação inválida, por favor selecione novamente a operação desjada.")
