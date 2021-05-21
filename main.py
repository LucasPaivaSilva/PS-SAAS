# Exercício de programação - PS SAAS
# Autor: Lucas Paiva da Silva

# Subsistema hipotético de gerenciamento de caixas eletrônicos
# Responsável por contabilizar e liberar as notas existentes no caixa eletrônico

# Importa a classe CaixaEletronico, localizada no arquivo caixaeletronico.py
from caixaeletronico import CaixaEletronico

# Criação do Caixa01
Caixa01 = CaixaEletronico()

# Saldo ficitio para testar o sistema
SaldoEmConta = 1000

# Variável de controle do loop do menu
ControleDoMenu = True

# Loop de escolha
while ControleDoMenu:
    print("")
    print('Bem vindo ao sistema bancario\n1.Sacar\n2.Abastecer o caixa\n3.Consultar dinheiro em caixa\n4.Sair')
    EscolhaDoUsuario = int(input("Sua escolha: "))

    # 1 -> Saque (verificação do saldo em conta e saque)
    if EscolhaDoUsuario == 1:
        print("Você escolheu efetuar um saque")
        ValorASerSacado = int(input("Quanto você gostaria de sacar? "))
        # Verifica se o usuário possúi o valor a ser sacado na connta 
        if ValorASerSacado>SaldoEmConta:
            print("Você não possuí saldo suficiente em conta para realizar esse saque!")
            continue
        Caixa01.sacarNotas(ValorASerSacado)

    # 2 -> Deposito (abasteciomento do caixa )
    elif EscolhaDoUsuario == 2:
        print("Você escolheu abastercer o caixa")
        Caixa01.carregarNotas(int(input("Valor da(s) nota(s): ")), int(input("Quantidade de nota(s) a serem inseridas: ")))

    # 3 -> Consulta dos valores em caixa
    elif EscolhaDoUsuario == 3:
        print("O valor em caixa é de: ", Caixa01.retornarValorEmCaixa())
        print("Disposto nas seguintes notas")
        Caixa01.mostrarCedulasEmCaixa()

    # 4 -> Sair e finalizar o programa
    elif EscolhaDoUsuario == 4:
        print("Você escolheu sair!")
        ControleMenu = False
    
    else:
        print("Entrada inválida, selecione 1,2,3 ou 4")
