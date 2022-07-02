#ex 4 (Industrias e poluição)

#Grupo de empresas 1
P_aceita =float(0.25)
Limite_poluição = float(0.3)
Industria1 = float(input("Industria I: Adicione aqui os dados de indice poluentes: "))
Industria2 = float(input("Industria II: Adicione aqui os dados de indice poluentes: "))
Industria3 = float(input("Industria III: Adicione aqui os dados de indice poluentes: "))
G1_Poluição_Total = (Industria1+Industria2+Industria3) / 3
if G1_Poluição_Total >= Limite_poluição:
   print(f' O indice de poluição do Grupo I é: {G1_Poluição_Total}, Atividades deste grupo suspenças.')
elif G1_Poluição_Total > P_aceita and G1_Poluição_Total < Limite_poluição:
    print(f' O indice de poluição do Grupo I é: {G1_Poluição_Total}, "ATENÇÃO" Seu grupo esta com altos indices poluentes!')
else: 
     print(f' O indice de poluição do Grupo I é: {G1_Poluição_Total}, Bom trabalho!')


#Grupo de empresas 2
Limite_poluição2 = float(0.4) 
Industria4 = float(input("Industria IV: Adicione aqui os dados de indice poluentes: "))
Industria5 = float(input("Industria V: Adicione aqui os dados de indice poluentes: "))
Industria6 = float(input("Industria VI: Adicione aqui os dados de indice poluentes: "))
G2_Poluição_Total = (Industria4+Industria5+Industria6) / 3

if G2_Poluição_Total >= Limite_poluição2:
   print(f' O indice de poluição do Grupo II é: {G2_Poluição_Total}, Atividades dos Grupos I e II suspenças.')

elif G2_Poluição_Total > P_aceita and G2_Poluição_Total < Limite_poluição2:
    print(f' O indice de poluição do Grupo II é: {G2_Poluição_Total}, "ATENÇÃO" Seu grupo esta com altos indices poluentes!')

else: 
    print(f' O indice de poluição do Grupo I é: {G2_Poluição_Total}, Bom trabalho!')


#Grupo de empreas 3 
Limite_poluição3 = float(0.5) 
Industria7 = float(input("Industria VII: Adicione aqui os dados de indice poluentes: "))
Industria8 = float(input("Industria VIII: Adicione aqui os dados de indice poluentes: "))
Industria9 = float(input("Industria IX: Adicione aqui os dados de indice poluentes: "))
G3_Poluição_Total = (Industria7+Industria8+Industria9) / 3
print(f"O indice de poluição do Grupo III é {G3_Poluição_Total}")

if G3_Poluição_Total >= Limite_poluição3:
    print(f' O indice de poluição do Grupo III é: {G3_Poluição_Total}, Atividades de todos os Grupos Suspenças.')

elif G3_Poluição_Total > P_aceita and G3_Poluição_Total < Limite_poluição3:
    print(f' O indice de poluição do Grupo III é: {G3_Poluição_Total}, "ATENÇÃO" Seu grupo esta com altos indices poluentes!')

else: 
     print(f' O indice de poluição do Grupo III é: {G3_Poluição_Total}, Bom trabalho!')


#condição geral 
All_Grupos = (G1_Poluição_Total + G2_Poluição_Total + G3_Poluição_Total)
print(f"O indice de poluição gerada pelas empresas é: {All_Grupos}")