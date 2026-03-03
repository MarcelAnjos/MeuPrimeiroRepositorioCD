print("Fechamento de caixa inicializando...")
fechamento = 1
total = 0
contador=0
forma=0
while fechamento == 1:
    produto = float(input("Insira o valor do produto: "))
    while produto <=0:
        produto = float(input("Por favor Insira um valor valido: "))
    print("Adicionando produto....")
    total+=produto
    contador+=1
    fechamento = int(input("Para adicionar mais produtos digite 1 se nao 0: "))
    while fechamento <0:
        fechamento(int(input("por favor digite um valor valido: ")))
    while fechamento == 0:
        print("Fechando registro do caixa...")
        forma= int(input("Escolha a forma de pagamento:\n1- Dinheiro \n2- Cartao \n Digite: "))
        while forma== 1:
            desconto= total *0.95
            media = desconto/contador
            print("Dinheiro selecionado-\n Calculando Desconto..")
            print("Gerando a conta...")
            print(f"O valor total da conta ficou: R${desconto:.2f}")
            print(f"A quantidade total de produto comprados foi: {contador}")
            print(f"A media de preco de cada produto è: R${media:.2f}")
            break         
        while forma ==2:
            media=total/contador
            print("Cartao Selecionado-")
            print("Gerando a conta...")
            print(f"O valor total da conta ficou: R${total:.2f}")
            print(f"A quantidade total de produto comprados foi: {contador:.2f}")
            print(f"A media de preco de cada produto è: R${media:.2f} ")
            break
        break