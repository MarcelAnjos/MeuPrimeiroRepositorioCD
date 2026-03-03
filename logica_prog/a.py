nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
media = (nota1 + nota2)/2

if media >= 7:
    print('Aluno Aprovado!!!')
    print('     A media do aluno foi:', media)
    
else:
    print('Aluno Reprovado :( ')
    print('     A media do aluno foi:', media)