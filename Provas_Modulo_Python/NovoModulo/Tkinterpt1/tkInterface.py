'''[PT-A08] 
Você foi contratado por uma empresa de gestão comercial para realizar a construção de uma sistema de lista telefônica usando o framework Tkinter com a linguagem Python,Seu objetivo é possibilitar ao usuário a inserção de duas informações: o nome e o telefone do novo contato. Em seguida, ao clicar no botão “cadastrar” será ativo um FileDialog que possibilite a criação de um novo arquivo para o salvamento dos dados. Além disso, verifique a cada nova inserção se o usuário já possui um arquivo para salvamento de dados criado, evitando que a cada novo contato seja aberto um novo fileDialog, através de uma variável de controle. Com base nos comandos anteriores construa e desenvolva esse código.'''

from tkinter import*
from tkinter import ttk
from metodos import *

app = Tk()
date = {}
#Configurações da tela principal
app.title('Empresa')
app.configure(background='#1e3743')
app.geometry('350x400')
app.resizable(False,False)

#cabeçalho + label & entrys
header = Label(app, text = 'Registro Telefônico',bg = '#1e3743',fg= '#ffffff')
header.configure(font = ('Courier',14))
header.place(relx = 0.2, rely= 0.1)

Namelb = Label(app, text = 'Nome',bg = '#1e3743',fg= '#ffffff')
Namelb.configure(font = ('Courier',12))
Namelb.place(relx = 0.1, rely= 0.3)
NameEntry = Entry(app)
NameEntry.place(relx = 0.1, rely = 0.38, relwidth = 0.7)


Tellb = Label(app, text = 'Tel',bg = '#1e3743',fg= '#ffffff')
Tellb.configure(font = ('Courier',12))
Tellb.place(relx = 0.1, rely= 0.48)
TelEntry = Entry(app)
TelEntry.place(relx = 0.1, rely = 0.56, relwidth = 0.4)


Footer = Label(app, text = 'Github - stun106')
Footer.place(relx = 0.73, rely = 0.95)

#button
Btn = ttk.Button(app,text = 'R E G I S T R A R', command = lambda:salvar([
                                                                        NameEntry.get(),
                                                                        TelEntry.get()
                                                                                ]))
Btn.place(relx = 0.35, rely= 0.75)

def salvar(lista:list):
    Query(lista,date,NameEntry)
    ClearEntry(NameEntry,TelEntry)
    
app.mainloop()




    





