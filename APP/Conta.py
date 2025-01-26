class Conta:
    def __init__(self, titular, numero, saldo=0):
        """
        Inicializa uma conta bancária com os dados do titular, número da conta e saldo inicial.

        Args:
            titular (str): Nome do titular da conta.
            numero (int): Número da conta.
            saldo (float): Saldo inicial da conta (padrão é 0).
        """

        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Define um novo valor para o saldo, garantindo que não seja negativo.

        Args:
            valor (float): Novo valor do saldo.

        Raises:
            ValueError: Se o valor informado for negativo.
        """
        if valor < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = valor

    def saque(self, valor):
        """
        Realiza um saque na conta, se houver saldo suficiente.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque for bem-sucedido, False caso contrário.
        """
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def deposita(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.
        """
        self._saldo += valor
        print(f"Depósito de {valor} realizado com sucesso.")

    def extrato(self):
        """
        Exibe o extrato da conta com o titular e o saldo atual.
        """
        print(f"Cliente: {self._titular}, Saldo Atual: {self._saldo}")
