nome = input("Informe o seu nome: ")
print(f"Olà {nome}, eu sou o Prime e estou aqui para descobrir o seu perfil como cliente!!\nPor favor, responda as questoes de maneira honesta, para melhor resultado!\n")
print("Qual sua renda mensal? em R$")
renda = float(input("Minha renda mensal è: R$"))
print("Qual seu gasto mensal? em R$")
gasto = float(input("Meu gasto mensal è: R$"))
reserva = 0
investimento =""
saldo= renda - gasto
if gasto > renda:
    print("Alerta: Emergencia Financeira!")
    print("Seus gastos estáo maiores que sua renda.")
else:
    print("Boa notícia! Você tem superávit mensal de: R$", saldo)
    reserva = gasto*6

while True:
    print("Agora eu quero saber de 0 à 10, qual sua coragem em relacao a investimentos? ")
    coragem = int(input("Minha coragem è nivel: "))
    if coragem <4:
        investimento = "Tesouro Direto."
        break
    elif 4 <= coragem <= 7:
        investimento ="Fundos Imobiliarios."
        break
    elif coragem >7 and coragem <11:
        investimento ="Ações de Tecnologia."
        break
    else:
        print("ERRO: VALOR DA CORAGEM INVALIDO!\n")
        
print("Agora eu quero saber, por quantos anos vocë pretende investir? ")
anos = input(f"Eu pretendo investir por: ")

if saldo > 0:
    valor_final = saldo * 12 * anos
    print(f"\n Se você investir seu superávit por {anos} anos, poderá acumular cerca de R$ {valor_final:.2f} (sem considerar juros).")