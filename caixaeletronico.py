class CaixaEletronico:
    # Construtor da classe
    def __init__(self):
        # Criação de um dicionário para armazenar as celulas do sistema e as quantidades das mesmas
        self.Notas = {10: 5, 20: 1, 50: 0, 100: 0}

    # Método para carregar as notas
    def carregarNotas(self, ValorDaNota, QuantidadeDeNotas):
        if (ValorDaNota in self.Notas and QuantidadeDeNotas != 0):
            self.Notas[ValorDaNota] += QuantidadeDeNotas
            print(QuantidadeDeNotas, "nota(s) de", ValorDaNota, "foram abastecidas")
        else:
            print("Valor da nota inválido e/ou Tentativa de abastecer 0 nota(s)")

    # Método para retornar a quantidade de dinheiro no caixa
    def retornarValorEmCaixa(self):
        ValorEmCaixa = 0
        for ValorDaNota in self.Notas:
            ValorEmCaixa += ValorDaNota * self.Notas[ValorDaNota]
        return ValorEmCaixa

    # Método mostrar a quantidade de cada uma das notas presentes no caixa
    def mostrarCedulasEmCaixa(self):
        for ValorDaNota in self.Notas:
            print(self.Notas[ValorDaNota], "nota(s) de", ValorDaNota)

    # Método para sacar as notas
    def sacarNotas(self, ValorASerSacado):
        if ValorASerSacado > self.retornarValorEmCaixa():
            print("Saque negado! Quantidade insuficiente em caixa")
            return False     
        else:
            # Criação de uma cópia do dicionário, feito para não interferir com a princípal em certas lógicas
            VetorDeNotas = self.Notas.copy()
            CopiaDeValorASerSacado = ValorASerSacado
            SaqueInvalido = False
            # Caso o valor solicitado tenha um resto diferente do que 0, não será possível distribui o mesmo com as notas no caixa 
            if ValorASerSacado%10 != 0:
                SaqueInvalido = True
            # Começa a distribuição das notas de cima para baixo, o motivo disso está explicado no readme.md
            for ValorDaNota in reversed(VetorDeNotas):
                # Caso o valor a ser sacado seja maior que a nota sendo destribuída, passa para a próxima nota
                if ValorDaNota > ValorASerSacado:
                    continue
                # Verifica se ainda existem notas a serem distribuidas e se o valor já não foi alcançado
                while VetorDeNotas[ValorDaNota] != 0 and ValorASerSacado > 0:
                    # Passa para próxima nota ou invalida o saque no caso das notas não poderem completar a quantia solicitada 
                    if ValorASerSacado - ValorDaNota < 0:
                            if ValorDaNota > ValorASerSacado:
                                break
                            else:
                                SaqueInvalido = True
                                break
                    # Desconta cada nota do valor a ser sacado, faz o desconto na cópia do dicionário
                    ValorASerSacado -= ValorDaNota 
                    VetorDeNotas[ValorDaNota]  = VetorDeNotas[ValorDaNota] - 1
            if SaqueInvalido:
                print("Saque negado! Notas não permitem completar a quantia solicitada")
                return False
            else:
                # Caso o saque seja válido, mostra as notas utilizadas 
                print("Saque de", CopiaDeValorASerSacado, "reais aprovado\nAs notas ejetadas foram:")
                for ValorDaNota in self.Notas:
                    print(self.Notas[ValorDaNota] - VetorDeNotas[ValorDaNota], "nota(s) de", ValorDaNota)
                # Transfere os valores da cópia para o dicionário original 
                self.Notas = VetorDeNotas
                return True