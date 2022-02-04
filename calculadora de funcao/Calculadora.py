from tkinter import *
from tkinter import ttk
from Reformat import reformat_code
from true_evaluate import *


##functions
def print_list():
    lbl["text"]=str(true_evaluate(reformat_code(var.get())))

##root
root=Tk()
root.title("Calculadora de função")

##mainframe
mainframe=ttk.Frame(master=root, width="500px", height="700px")
mainframe.grid()
mainframe.grid_propagate(False)
mainframe.grid_columnconfigure(index=0, weight=1)
mainframe.grid_columnconfigure(index=1, weight=0)
mainframe.grid_rowconfigure(index=2, weight=1)

##variables
var=StringVar(value="")
output=StringVar(value="")


##widgets
ttk.Label(master=mainframe, text="Digite um polinômio:").grid(column=0, row=0, sticky="e")
ttk.Entry(master=mainframe, textvariable=var).grid(column=1, row=0, sticky="w")

lbl=ttk.Label(master=mainframe, text="", wraplength=400)


ttk.Button(master=mainframe,text="Printar",command=print_list).grid(column=0, row=1, sticky="ne")
lbl.grid(column=0, row=2, sticky="ewsn", columnspan=2)

##mainloop
mainloop()
