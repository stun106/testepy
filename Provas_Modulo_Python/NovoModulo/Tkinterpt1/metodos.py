from tkinter import *
def ClearEntry(NameEntry,TelEntry) -> None:
    NameEntry.delete(0,END)
    TelEntry.delete(0,END)
   
def Query(lista:list,date:dict):
    if '' in lista:
        print('Erro, Verifique seus Dados')
    elif lista[0] in date.values() or lista[1] in date.values():
        print('redundancia de dados')
    else:        
        date['Cliente']= lista[0]
        date['Telefone'] = lista[1]
        print(date)


    


        
      
    