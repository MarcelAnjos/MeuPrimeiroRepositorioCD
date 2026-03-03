vendas_brutas = [
    (101, "Monitor", 5, 1200.0),
    (102, "Mouse", 50, 80.0),
    (103, "Teclado", 8, 150.0),
    (104, "Case", 3, 50.0)
]

reajuste = 0.10  #=

vendas_atualizadas = [
    (id_prod, nome, qtd, preco * (1 + reajuste))
    for (id_prod, nome, qtd, preco) in vendas_brutas
]

print("Lista atualizada com reajuste:")
for item in vendas_atualizadas:
    print(item)