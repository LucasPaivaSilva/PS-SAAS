class CaixaEletronico:
    def __init__(self):
        self.Notas = {10: 5, 20: 1, 50: 0, 100: 0}

    def carregarNotas(self, ValorDaNota, QuantidadeDeNotas):
        if (ValorDaNota in self.Notas and QuantidadeDeNotas != 0):
            self.Notas[ValorDaNota] += QuantidadeDeNotas
            print(QuantidadeDeNotas, "notas de", ValorDaNota, "foram abastecidas")
        else:
            print("Valor da nota inválido e/ou Tentativa de abastecer 0 notas")

    def retornarValorEmCaixa(self):
        ValorEmCaixa = 0
        for ValorDaNota in self.Notas:
            ValorEmCaixa += ValorDaNota * self.Notas[ValorDaNota]
        return ValorEmCaixa

    def mostrarCedulasEmCaixa(self):
        for ValorDaNota in self.Notas:
            print(self.Notas[ValorDaNota], "notas de", ValorDaNota)

    def sacarNotas(self, ValorASerSacado):
        if ValorASerSacado > self.retornarValorEmCaixa():
            print("Saque negado! Quantidade insuficiente em caixa")      
        else:
            VetorDeNotas = self.Notas.copy()
            CopiaDoValorASerSacado = ValorASerSacado
            SaqueInvalido = False
            print(CopiaDoValorASerSacado)
            for ValorDaNota in reversed(VetorDeNotas):
                if ValorDaNota > ValorASerSacado:
                    continue
                while VetorDeNotas[ValorDaNota] != 0 and CopiaDoValorASerSacado > 0:
                    if CopiaDoValorASerSacado - ValorDaNota < 0:
                        SaqueInvalido = True
                        break
                    CopiaDoValorASerSacado -= ValorDaNota 
                    VetorDeNotas[ValorDaNota]  = VetorDeNotas[ValorDaNota] - 1
                    print(CopiaDoValorASerSacado)
            for ValorDaNota in VetorDeNotas:
                print(VetorDeNotas[ValorDaNota], "notas de", ValorDaNota)
            if SaqueInvalido:
                print("Saque negado! Notas não permitem completar a quantia solicitada")
            else:
                self.Notas = VetorDeNotas

            




                
            



            





