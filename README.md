# Código do processo seletivo do SAAS - Lucas Paiva da Silva

Considerando um sistema hipotético de gerenciamento interno de caixas eletrônicos.\
O código atua como um subsistema responsável por contabilizar e liberar as notas existentes no caixa eletrônico.

## Requisitos

- Registro do abastecimento de notas de 10,20,50 e 100 reais 
- Verificação da validade do saque (quantia em caixa, número de notas e saldo do cliente
- Informação das notas a serem liberadas em um saque válido 

## Loop de Distribuição/Saque
A distribuição das notas começa com as notas mais altas, uma das razões sendo a priorização das notas "menores", pois\
essas tem maior demanda e saída. 
```python
  for ValorDaNota in reversed(VetorDeNotas):
                # Caso o valor a ser sacado seja maior que a nota sendo destribuída, passa para a próxima nota
                if ValorDaNota > ValorASerSacado:
                    continue
                # Verifica se ainda existem notas a serem distribuidas e se o valor já não foi alcançado
                while VetorDeNotas[ValorDaNota] != 0 and ValorASerSacado > 0:
                    # Invalida o saque no caso das notas não poderem completar a quantia solicitada 
                    if ValorASerSacado - ValorDaNota < 0:
                        SaqueInvalido = True
                        break
                    # Desconta cada nota do valor a ser sacado, faz o desconto na cópia do dicionário
                    ValorASerSacado -= ValorDaNota 
                    VetorDeNotas[ValorDaNota]  = VetorDeNotas[ValorDaNota] - 1
```



