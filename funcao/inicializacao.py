# 2. Tratamento de Dados (Função “limpar_vendas”):
# • Crie uma função que receba a lista de vendas da filial.
# • A função deve retornar uma nova lista contendo apenas valores que sejam
# maiores que 0 e menores que 10.000.

def limpar_vendas(clean):
    tamanho = len(clean)
    lista = [clean for clean in range(tamanho) if tamanho < 10.000 and tamanho>0]
    return lista

def analisar_dados(anl):
    lista = []
    lista = sum(lista)
    return lista

lista=[1,2,3]

print(analisar_dados(lista))