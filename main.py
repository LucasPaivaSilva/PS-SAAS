
from caixaeletronico import CaixaEletronico

Caixa01 = CaixaEletronico()

while True:
    print('1.Sacar\n2.Abastecer o caixa\n3.Consultar dinheiro em caixa\n4.Sair')
    EscolhaDoUsuario = int(input("Sua escolha: "))
    if EscolhaDoUsuario == 1:
        print("Você escolheu efetuar um saque")
        Caixa01.sacarNotas(int(input("Quanto você gostaria de sacar? ")))

    elif EscolhaDoUsuario == 2:
        print("Você escolheu abastercer o caixa")
        Caixa01.carregarNotas(int(input("Valor da nota que será inserida: ")), int(input("Quantidade de notas a serem inseridas: ")))

    elif EscolhaDoUsuario == 3:
        print("O valor em caixa é de: ", Caixa01.retornarValorEmCaixa())
        print("Disposto nas seguintes notas")
        Caixa01.mostrarCedulasEmCaixa()

    else:
        print("Você escolheu sair!")
        break
    
    print("\n")