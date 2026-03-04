# Identidade e Atribuição: Comece com um saldo_inicial = 1000.0. Crie
# uma variável checkpoint = saldo_inicial. Use o operador is para confirmar
# que o checkpoint aponta para o mesmo local de memória.

saldo_inicial = 1000.0
checkpoint = saldo_inicial
print(checkpoint is saldo_inicial)

# 2. Repetição e Associação: O programa deve pedir ao usuário o nome do
# auditor. Verifique se o nome contém caracteres proibidos
# como * ou # usando o operador in. Se tiver, peça para digitar novamente
# (WHILE).
# Programa que solicita o nome do auditor
# e verifica se contém caracteres proibidos (* ou #)

nome = input("Digite o nome do auditor: ")

while "*" in nome or "#" in nome:
    print("Nome inválido! Não use os caracteres * ou #.")
    nome = input("Digite o nome do auditor novamente: ")

print("Nome cadastrado com sucesso:", nome)

# 3. Processamento de Lote (FOR): O programa deve processar exatamente 4
# transações. Para cada transação, o usuário insere o valor (positivo para
# crédito, negativo para débito).

saldo_atual = saldo_inicial

for i in range(4):
    valor = float(input(f"Digite o valor da transação {i+1}: "))

    # 4. Condicionais e Lógica:

    # a. Se o valor for maior que 500.0, exiba um alerta.
    if valor > 500.0:
        print("Transação de alto valor!")

    # b. Se o valor for negativo e o saldo atual for insuficiente para cobri-lo,
    # a transação deve ser ignorada.
    if valor < 0 and saldo_atual + valor < 0:
        print("Erro: saldo insuficiente. Transação ignorada.")
        continue

    saldo_atual += valor

# 5. Resultado Final: Exiba o saldo final e verifique se ainda é o mesmo objeto do checkpoint.

saldo_final = saldo_atual

print("\nSaldo Final:", saldo_final)
print("saldo_final is checkpoint:", saldo_final is checkpoint)