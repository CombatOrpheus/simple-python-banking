import unittest
from banking import ContaBancaria
import io
import sys

class TestContaBancaria(unittest.TestCase):

    def setUp(self):
        """Cria uma nova instância de ContaBancaria para cada teste."""
        self.conta = ContaBancaria(saldo_inicial=1000, limite=500, limite_saques=3)

    def test_deposito(self):
        """Testa a função de depósito."""
        self.conta.deposito(500)
        self.assertEqual(self.conta.saldo, 1500)
        self.assertIn("Depósito: R$500.00\n", self.conta.extrato)

    def test_deposito_valor_negativo(self):
        """Testa a função de depósito com valor negativo."""
        self.conta.deposito(-100)
        self.assertEqual(self.conta.saldo, 1000)
        self.assertEqual(len(self.conta.extrato), 0)

    def test_saque(self):
        """Testa a função de saque."""
        self.conta.saque(200)
        self.assertEqual(self.conta.saldo, 800)
        self.assertEqual(self.conta.numero_saques, 1)
        self.assertIn("Saque: R$200.00\n", self.conta.extrato)

    def test_saque_saldo_insuficiente(self):
        """Testa o saque com saldo insuficiente."""
        self.conta.saque(1200)
        self.assertEqual(self.conta.saldo, 1000)
        self.assertEqual(self.conta.numero_saques, 0)

    def test_saque_excede_limite(self):
        """Testa o saque que excede o limite."""
        self.conta.saque(600)
        self.assertEqual(self.conta.saldo, 1000)
        self.assertEqual(self.conta.numero_saques, 0)

    def test_saque_excede_numero_saques(self):
        """Testa o saque que excede o número de saques."""
        self.conta.saque(100)
        self.conta.saque(100)
        self.conta.saque(100)
        self.conta.saque(100)
        self.assertEqual(self.conta.saldo, 700)
        self.assertEqual(self.conta.numero_saques, 3)

    def test_alterar_limite(self):
        """Testa a alteração do limite de saque."""
        self.conta.alterar_limite(1000)
        self.assertEqual(self.conta.limite, 1000)
        self.assertIn("Alteração de limite. Novo valor: R$1000.00", self.conta.extrato[-1])

    def test_adicionar_limite_saques(self):
        """Testa a adição ao limite de saques."""
        self.conta.adicionar_limite_saques(2)
        self.assertEqual(self.conta.limite_saques, 5)

    def test_exibir_extrato(self):
        """Testa a exibição do extrato."""
        self.conta.deposito(200)
        self.conta.saque(100)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.conta.exibir_extrato()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Depósito: R$200.00", output)
        self.assertIn("Saque: R$100.00", output)
        self.assertIn("Saldo: R$ 1100.00", output)

if __name__ == '__main__':
    unittest.main()
