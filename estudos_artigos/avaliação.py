#Prova Introdução ao Python e Estrutura Condicional
'''Questão 1'''
#1. [LP-A03] Crie um algoritmo que recebe como entrada o dia e o mês de nascimento e retorna o signo, seguindo as faixas de valores informados:
#  - Áries: de 21 março a 20 abril;- 
# Touro: de 21 abril a 20 maio; - 
# Gêmeos: de 21 maio a 20 junho; - 
# Câncer: de 21 junho a 22 julho; -
#  Leão: de 23 julho a 22 agosto; -
#  Virgem: de 23 agosto a 22 setembro; -
#  Libra: de 23 setembro a 22 outubro; -
#  Escorpião: de 23 outubro a 21 novembro; 
# - Sagitário: de 22 novembro a 21 dezembro; 
# - Capricórnio: de 22 dezembro a 20 janeiro;
#  - Aquário: de 21 janeiro a 18 fevereiro; 
# - Peixes: de 19 fevereiro a 20 março.


while True:
    sIgNoS = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']    
    DaY= int(input('Dia de Nascimento: '))    
    moUnTh = str(input('Mês de Nascimento: '))    
    confirme = str(input('Digite "Y" para continuar: ')).lower()    
    if confirme != 'y':       
        print('Siga as instruções a cima!')    
    elif DaY >= 21 and moUnTh == 'janeiro' or  moUnTh == 'fevereiro' and DaY <=18:        
        print(sIgNoS[10])        
        break    
    elif DaY >= 19 and moUnTh == 'fevereiro' or moUnTh == 'março' and DaY <= 20:  
        print(sIgNoS[11])       
        break   
    elif DaY >= 21 and moUnTh == 'março' or moUnTh == 'abril' and DaY <= 20:       
        print(sIgNoS[0])  
        break    
    elif DaY >= 21 and moUnTh == 'abril' or moUnTh == 'maio' and DaY <= 20: 
        print(sIgNoS[1])
        break 
    elif DaY >= 21 and moUnTh == 'junho' or moUnTh == 'julho' and DaY <= 22:
        print(sIgNoS[3])       
        break    
    elif DaY >= 23 and moUnTh == 'julho' or moUnTh == 'agosto' and DaY <= 22:
        print(sIgNoS[4])        
        break    
    elif DaY >= 23 and moUnTh == 'agosto' or moUnTh == 'setembro' and DaY <= 22:
        print(sIgNoS[5])       
        break    
    elif DaY >= 23 and moUnTh == 'setembro' or moUnTh == 'outubro' and DaY <= 22:
        print(sIgNoS[6]) 
        break    
    elif DaY >= 23 and moUnTh == 'outubro' or moUnTh == 'novembro' and DaY <= 21:
        print(sIgNoS[7])       
        break    
    elif DaY >= 22 and moUnTh == 'novembro' or moUnTh == 'dezembro' and DaY <= 21:        
        print(sIgNoS[8])        
        break    
    else:         
        print(sIgNoS[9])        
        break