from tkinter import *
from WebScrapping import *

class Tela(Tk):
    webscrapping = WebScrapping()

    def __init__(self):
        super().__init__()
        frameBusca = Frame(self,)
        frameBusca.pack()

        labelItem = Label(frameBusca,text='Item:')
        labelItem.grid(row=0,column=0)
        self.entryItem = Entry(frameBusca)
        self.entryItem.grid(row=0,column=1)
        botaoBusca = Button(frameBusca,text='Buscar',command=self.buscar)
        botaoBusca.grid(row=1,columnspan=2,sticky=W+E,padx=6)


    def buscar(self):
        item = self.entryItem.get()
        self.webscrapping.buscar(item)





