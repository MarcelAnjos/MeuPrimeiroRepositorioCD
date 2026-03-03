# 1. Integração: Operadores + Condicionais:
# Exercício: Peça ao usuário seu peso (kg) e altura (m). Calcule o IMC (peso/altura2
# ).

# Em seguida, utilize uma estrutura if/elif/else para exibir a classificação:
# • Menor que 18.5: Abaixo do peso
# • Entre 18.5 e 24.9: Peso normal
# • Entre 25.0 e 29.9: Sobrepeso
# • 30.0 ou mais: Obesidade
# Dica: Use operadores de comparação encadeados (ex: 18.5 <= imc < 25).
peso = float(input("Informe o seu peso em (kg): "))
altura = float(input("Informe a sua altura em (m): "))
imc = peso/(altura*altura)
if imc <18.5:
    print(f"Abaixo do Peso")
elif imc >=18.5 and imc <=24.9:
    print("Peso Normal")
elif imc >=25.0 and imc <=29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 2. Integração: Repetição FOR + Operadores de Associação:
# Exercício: Peça para o usuário digitar uma frase ou nome completo. Utilizando um
# laço for, percorra cada caractere da string e verifique se ele é uma vogal (utilizando
# o operador in "aeiouAEIOU"). Ao final, exiba o total de vogais encontradas.

texto = input("Digite uma frase ou nome completo: ")

contador_vogais = 0

for caractere in texto:
    contador_vogais += caractere in "aeiouAEIOU"
print(f"Total de vogais encontradas: {contador_vogais}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 3. Integração: Repetição WHILE + Condicionais + Atribuição:
# Exercício: Crie um programa que inicialize uma variável saldo = 500.0. Exiba um
# menu com as opções: (1) Depositar, (2) Sacar e (3) Sair.
# • Se escolher depositar, peça o valor e some ao saldo.
# • Se escolher sacar, verifique se há saldo suficiente; se sim, subtraia; se não,
# avise "Saldo Insuficiente".
# • O programa deve repetir (while) até que o usuário escolha a opção 3.

saldo = 500.0
deposito=0
escolha=0
saque=0
print("Bem vindo ao Caixa Eletronico!!")
while escolha != 3:
    escolha = int(input("O que deseja fazer - \n(1)-Depositar\n(2)-Sacar\n(3)-Sair\n digite:  "))
    if escolha == 1:
        deposito = float(input("Digite o valor do deposito? : "))
        saldo = deposito+saldo
        print(f"Deposito feito com sucesso!!\nValor atual da conta: {saldo}")
    elif escolha ==2:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            print(f"Saldo Insuficiente!!\nSaldo Atual: {saldo}\nValor do Saque: {saque}")
        else:
            saldo = saldo-saque
            print(f"Saque feito com sucesso!!\nValor atual da conta: {saldo}")
    elif escolha ==3:
        print("OBRIGADO POR UTILIZAR O NOSSO CAIXA ELETRONICO!!!!\n VOLTE SEMPRE!!!!!")

# 4. Integração: Identidade + Coleções Simples:
# Exercício: Na Ciência de Dados, entender se estamos copiando um dado ou
# apenas criando uma referência é vital.
# Crie uma lista dados_originais = [10, 20, 30].
# 1. Crie dados_referencia = dados_originais.
# 2. Crie dados_copia = [10, 20, 30].

# Use o operador is para mostrar ao aluno que dados_referencia é o mesmo
# objeto que o original, mas dados_copia não é, apesar de terem valores
# idênticos.

dados_originais = [10, 20, 30]
dados_referencia = dados_originais
dados_copia = [10, 20, 30]

print(f"Dados referencia è igual aos dados originais: {dados_referencia is dados_originais}\ndados_copia nao è igual aos dados originais: {dados_copia is not dados_originais} ")