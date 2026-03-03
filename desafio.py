import random
print("EXPLORAÇÃO DO PLANETA – APLICAÇÃO DE FUNÇÃO")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" Em um futuro distante, a humanidade alcançou as estrelas e iniciou a exploração de planetas distantes. A bordo da nave intergaláctica 'Exploradora Estelar',    uma tripulação composta por cientistas, engenheiros e aventureiros chega ao planeta Alphara-7, um mundo misterioso repleto de paisagens alienígenas.")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" Ao aterrissar em Alphara-7, a tripulação sente a expectativa no ar. Equipados com trajes espaciais avançados, eles  começam a explorar a superfície do planeta,  ansiosos por desvendar seus segredos.")
#passo (1) Início:
mineral=0


alien=0
explore =0
while True:
    sorte=0
    print("Ao aterrissar em Alphara-7, a tripulação sente a expectativa no ar.Equipados com trajes espaciais avançados, eles começam a explorar a superfície do planeta, ansiosos por desvendar seus segredos.")
#Passo (2) Condição de Exploração:
    print("Iniciando fase de exploracao!")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Apos alguns minutos explorando a superfìcie do planeta a equipe se deparou com seu primeiro grande obstaculo... UMA MONTANHA ENORME!! e voce como lider do esquedrao precisa decidir qual serà o proximo passo da equipe. ")
    missao = 1
    while missao == 1:
        explore =int(input("Decida o que a equipe irà fazer!\n (1)-Escalar Montanha\n (2)-Contornar Montanha\nDigite: "))
        if explore ==1:
            print("Vocë como lider decidiu que a equipe deve escalar a montanha!!!")
            sorte = random.randint(1,10)
            if sorte > 5 and sorte <8:
                print("A equipe està tento sucesso ao escalar a montanha, mas infelizmente ainda nao fizeram nenhuma descoberta :c")
                print("---------------------------------------------------------------------------------------------------------------------------")   
                sorte = 0
            elif sorte >7 and sorte <10:
                print("PARABENS!!!!!!!!!!!!\n Durante a escala sua equipe descobriu uma area rica em minerais!")
                escolha=int(input("A equipe coleta dados científicos valiosos na área identificada. Em seguida, voce deve decidir se  a equipe deve prosseguir ou retornar à nave.\n(1)-Prosseguir\n(2)-Retornar\nDecida: "))
                mineral+=1
                if escolha == 2:
                    print("--------------------------------------------------------------------------------------------------------------------------------")    
                    print(f"A tripulação retorna à Exploradora Estelar e parte de volta para a Terra,trazendo consigo as descobertas incríveis feitas durante a expedição.\n Total de minerios encontrados: {mineral}\n Total de Aliens encontrados {alien}")
                    explore=0
                    sorte =0
                    break
            
            elif sorte ==10:
                print("PARABENS!!!!!!!!!!!!\n WOW WOW WOW WOW\n durante a escala sua equipe descobriu ALIENS!!!")
                escolha=int(input("A equipe coleta dados científicos valiosos na área identificada. Em seguida, voce deve decidir se  a equipe deve prosseguir ou retornar à nave.\n(1)-Prosseguir\n(2)-Retornar\nDecida: "))
                alien+=1
                if escolha == 2:
                    print("--------------------------------------------------------------------------------------------------------------------------------")    
                    print(f"A tripulação retorna à Exploradora Estelar e parte de volta para a Terra,trazendo consigo as descobertas incríveis feitas durante a expedição.\n Total de minerios encontrados: {mineral}\n Total de Aliens encontrados {alien}")
                    explore=0
                    sorte =0
                    break
            else:
                print("Durante a escalada da montanha houve uma VENTANIA MONSTRUOSA!!!!!\n o seu esquadrao acabou caindo da montanha!!!----VOCËS FALHARAM") 
                print("---------------------------------------------------------------------------------------------------------------------------")   
        elif explore == 2:
            print("Voce como lider decidiu que a equipe deve contornar a montanha!")
            sorte = random.randint(1,10)
            if sorte >3:
                print("PARABENS!!!!!!!!!!!!\n Durante o contorno da montanha sua equipe descobriu uma area rica em minerais!")
                escolha=int(input("A equipe coleta dados científicos valiosos na área identificada. Em seguida, voce deve decidir se  a equipe deve prosseguir ou retornar à nave.\n(1)-Prosseguir\n(2)-Retornar\nDecida: "))
                mineral+=1
                if escolha == 2:
                    print("--------------------------------------------------------------------------------------------------------------------------------")    
                    print(f"A tripulação retorna à Exploradora Estelar e parte de volta para a Terra,trazendo consigo as descobertas incríveis feitas durante a expedição.\n Total de minerios encontrados: {mineral}")
                    explore=0
                    sorte =0
                    break
                else:
                     print("DURANTE O CONTORNO DA MONTANHA ACONTECEU UM TERREMOTO, A MEDICA DO ESQUADRAO SE LESIONOU E VOCËS TIVERAM QUE VOLTAR E ESPERAR ELA SE RECUPERAR!!- VOCES FALHARAM") 
                     print("---------------------------------------------------------------------------------------------------------------------------")     
    break