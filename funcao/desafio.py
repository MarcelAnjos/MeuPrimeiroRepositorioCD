def limpar_vendas(lista_vendas):
    # Retorna apenas valores maiores que 0 e menores que 10000
    return [venda for venda in lista_vendas if 0 < venda < 10000]


def analisar_dados(lista):
    total = sum(lista)
    
    if len(lista) > 0:
        media = total / len(lista)
    else:
        media = 0
    
    return (total, media)


def definir_status(media):
    if media > 5000:
        return "Alta Performance"
    elif 2000 <= media <= 5000:
        return "Performance Estável"
    else:
        return "Performance Crítica"

nome_empresa = input("Digite o nome da Filial: ")
print("Iniciando coleta de valores!")

saldo = []

while True:
    coleta = float(input(f"Digite o valor de coleta da filial {nome_empresa} (0 para encerrar): R$ "))
    
    if coleta == 0:
        break
    
    saldo.append(coleta)

vendas_validas = limpar_vendas(saldo)


total, media = analisar_dados(vendas_validas)

status = definir_status(media)


print("\n" + "=" * 40)
print(f"RELATÓRIO DE PERFORMANCE - {nome_empresa}")
print("=" * 40)
print(f"Status: {status}")
print(f"Faturamento Total: R$ {total:.2f}")
print(f"Média das Vendas: R$ {media:.2f}")

print("\nVendas Válidas:")
for i, venda in enumerate(vendas_validas, start=1):
    print(f"{i}. R$ {venda:.2f}")

print("=" * 40)