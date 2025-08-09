from typing import List, Callable, TypeVar

T = TypeVar('T')

class ContaBancaria:
    """
    Representa uma conta bancária com funcionalidades de depósito, saque,
    visualização de extrato e alteração de limite de saque.
    """
    def __init__(self, saldo_inicial: float = 0, limite: float = 500, limite_saques: int = 3):
        """
        Inicializa a conta bancária.

        Args:
            saldo_inicial (float): O saldo inicial da conta.
            limite (float): O limite para cada saque.
            limite_saques (int): O número máximo de saques permitidos.
        """
        self.saldo: float = saldo_inicial
        self.limite: float = limite
        self.extrato: List[str] = []
        self.numero_saques: int = 0
        self.limite_saques: int = limite_saques

    def deposito(self, valor: float) -> None:
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            mensagem = f'Depósito: R${valor:.2f}\n'
            self.extrato.append(mensagem)
            print(mensagem)
        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(self, valor: float) -> None:
        """
        Realiza um saque da conta, se as condições forem atendidas.

        Args:
            valor (float): O valor a ser sacado.
        """
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            mensagem = f'Saque: R${valor:.2f}\n'
            self.extrato.append(mensagem)
            self.numero_saques += 1
            print(mensagem)
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self) -> None:
        """Exibe o extrato de transações da conta."""
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.extrato:
                print(transacao, end="")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def alterar_limite(self, novo_limite: float) -> None:
        """
        Altera o limite de saque da conta.

        Args:
            novo_limite (float): O novo valor do limite de saque.
        """
        self.limite = novo_limite
        mensagem = f'Alteração de limite. Novo valor: R${novo_limite:.2f}'
        self.extrato.append(mensagem)
        print(mensagem)

    def adicionar_limite_saques(self, valor: int) -> None:
        """
        Adiciona mais saques ao limite de saques.

        Args:
            valor (int): O número de saques a serem adicionados.
        """
        self.limite_saques += valor
        print(f"Limite de saques aumentado para {self.limite_saques}.")


def parse_input(prompt: str, parsing_function: Callable[[str], T]) -> T:
    """
    Solicita uma entrada do usuário e a converte para o tipo desejado.

    Args:
        prompt (str): A mensagem a ser exibida para o usuário.
        parsing_function (Callable[[str], T]): A função para converter a entrada.

    Returns:
        T: O valor de entrada convertido.
    """
    while True:
        try:
            return parsing_function(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, utilize apenas números e '.'.")

def main() -> None:
    """Função principal que executa o programa de terminal bancário."""
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Alterar Limite de Saque
    [ls] Adicionar Limite de Saques
    [q] Sair
    => """

    conta = ContaBancaria()

    while True:
        opcao = input(menu).lower()
        if opcao == "d":
            valor = parse_input("Digite o valor do depósito: R$", float)
            conta.deposito(valor)
        elif opcao == "s":
            print(f'Limite para saques: R${conta.limite:.2f}')
            valor = parse_input("Digite o valor do saque: R$", float)
            conta.saque(valor)
        elif opcao == "e":
            conta.exibir_extrato()
        elif opcao == "l":
            novo_limite = parse_input("Digite o novo valor do limite de saque: R$", float)
            conta.alterar_limite(novo_limite)
        elif opcao == "ls":
            valor = parse_input("Digite o número de saques a adicionar ao limite: ", int)
            conta.adicionar_limite_saques(valor)
        elif opcao == "q":
            print("Finalizando programa.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
