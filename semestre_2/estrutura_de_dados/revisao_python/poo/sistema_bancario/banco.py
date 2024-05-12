from clientes import Cliente
from contas import Conta

cliente1 = Cliente("Eduardo", "04795139377", "88994234549")
cliente2 = Cliente("Luciana", "04707282300", "88992225425")
cliente3 = Cliente("Miguel", "03592197214", "8893420020")
cliente4 = Cliente("Melissa", "32135490211", "8892242321")

conta1 = Conta(1, 100, cliente1)
conta1.exibir_saldo()
conta1.depositar(200)
conta1.exibir_saldo()
conta2 = Conta(2, 1550.50, cliente2)
conta2.exibir_saldo()
conta2.sacar(1600)
conta2.exibir_saldo()
