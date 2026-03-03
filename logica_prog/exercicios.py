# Exercicios Operadores:
#  Exercício 1: Peça ao usuário dois números inteiros. Calcule e exiba a soma, a
#  diferença, o produto, a divisão real, a divisão inteira e o resto da divisão
#  (módulo) entre eles
n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
soma = n1+n2
dif = n1-n2
prod = n1*n2
divreal = n1/n2
divint = n1//n2
resto = n1%n2
print(f"A soma dos valores è igual à: {soma}\nA diferenca dos valores è igual à: {dif}\nO produto dos valores è igual à: {prod}\nA divisão real dos valores è igual à: {divreal}\nA divisao inteira dos valores è igual à: {divint}\nO resto da divisão dos valores è igual à: {resto}")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
#  Exercício2: Crie uma variável saldo com valor inicial de 1000. Utilize
# operadores de atribuição composta (como +=, -=, *=) para simular três
#  operações: um depósito de 500, um saque de 200 e um rendimento que
#  dobra o saldo atual. Exiba o resultado final.

mil = 1000
mil+=500
mil-=200
mil*=2
print(f"VocÉ tem um valor de: R${mil} na sua conta")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# Exercício3: Receba dois valores numéricos e retorne uma série de
# booleanos (True ou False) verificando se o primeiro é maior que o segundo,
# se são iguais e se o primeiro é diferente do segundo.

n1 = float(input("Insira o primeiro valor: "))
n2 = float(input("Insira o segundo valor: "))

print(f"O Primeiro valor è maior que o segundo ? : {n1>n2}\nOs valores de n1 e n2 são iguais ? : {n1==n2}\nO primeiro valor è diferente do segundo valor? : {n1!=n2}")
 
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# Exercício4: Um aluno só é aprovado se tiver presenca maior ou igual a
# 75 E media maior ou igual a 7.0. Receba esses dois valores e verifique se o
# aluno foi aprovado utilizando operadores lógicos.

n1 = float(input("Insira a Presenca do Aluno: %"))
n2 = float(input("Insira a media do aluno: "))
print("Aprovado:", n1 >= 75 and n2 >= 7.0)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Exercício5: Crie duas listas com os mesmos elementos, por exemplo: a = [1,
# 2] e b = [1, 2]. Crie uma terceira variável c = a. Use o operador de identidade
# para verificar se a é o mesmo objeto que b e se a é o mesmo objeto que c.

a = [1,2]
b = [1,2]
c = a
print(f"A variavel 'A' è o mesmo objeto da variavel 'B' ? : {a is b}\nA variavel 'A' è o mesmo objeto da variavel 'C' ? : {a is c}")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# Exercício6: Dada a string "Ciência de Dados", verifique se o
# caractere "D" está presente na frase e se a palavra "Python" não está
# presente.

frase = 'Ciência de Dados'
print(f"A palavra 'D' esta presente na frase: {frase}?\n {'D' in frase}\nA palavra 'Python' não esta presente na frase: {frase}?\n {'Python' not in frase}")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Exercicios Estrutura Condicional (IF, ELIF, ELSE):
# Exercício1: Desenvolva um programa que receba a idade de um nadador e
# classifique-o em uma das seguintes categorias:
# • Infantil: 5 a 12 anos;

# • Juvenil: 13 a 17 anos;
# • Adulto: 18 anos ou mais;
# • Inválido: Menor que 5 anos.

idade = int(input("Insira a idade do Atleta: "))

if idade >=5 and idade <=12:
    print("infantil")
elif idade >=13 and idade <=17:
    print("Juvenil")
elif idade >=18:
    print("Adulto")
else:
    print("Invalido")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Exercicio Estrutura de Repetição FOR:
# Exercício1: Peça um número inteiro ao usuário e exiba a tabuada de
# multiplicação desse número de 1 a 10 utilizando o laço for e a
# função range().
n1 = int(input("Digite um numero inteiro: "))
for i in range(1,11):
    print(f"{n1}*{i} = {n1*i}")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Exerciocio Estrutura de Repetição WHILE:
# Exercício1: Escreva um programa que peça ao usuário para digitar uma
# senha. O programa deve continuar pedindo a senha (repetição) até que o
# valor digitado seja igual a "python123". Quando acertar, exiba "Acesso
# Permitido".

senha = ""
while senha != "python123":
    senha = input("Digite a sua senha: ")
    print("SENHA INVALIDA!!!!!!!!\nTENTE OUTRA VEZ!!")
    if senha == "python123":
        print("Acesso Permitido")
