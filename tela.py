from tkinter import *
from tkinter import ttk

#Telas principais
root=Tk()
root.title("Calculadora")
frm=ttk.Frame(root)
frm_2=ttk.Frame(root,width=200,height=root.winfo_height())

#Variáveis
input=StringVar(frm, value="")
output=StringVar(frm, value="")

#Funções
def One   ():
        input.set(input.get() + "1")
def Two   ():
        input.set(input.get() + "2")
def Three ():
        input.set(input.get() + "3")
def Four  ():
        input.set(input.get() + "4")
def Five  ():
        input.set(input.get() + "5")
def Six   ():
        input.set(input.get() + "6")
def Seven ():
        input.set(input.get() + "7")
def Eight ():
        input.set(input.get() + "8")
def Nine  ():       
        input.set(input.get() + "9")
def Zero  ():
        input.set(input.get() + "0")
def Reset():
    input.set("")
def Add():
        input.set(input.get() + "+")
def Sub  ():
        input.set(input.get() + "-")
def Mult  ():
        input.set(input.get() + "*")
def Div  ():
        input.set(input.get() + "/")

def Compute():
        output.set(eval(input.get()))

def LessFunc():
        bt_mais_funcoes.config(text="+funções",command=MoreFunc)
        root.grid_columnconfigure(1, weight=0)
        frm_2.grid_forget()

def MoreFunc():
        frm_2.grid(column=1,row=0)
        root.grid_columnconfigure(1, weight=1)
        bt_mais_funcoes.config(text="-funções",command=LessFunc)




#Funções de binding
def OneKey   (event):
          bt_1.invoke()
def TwoKey   (event):
        input.set(input.get() + "2")
def ThreeKey (event):
        input.set(input.get() + "3")
def FourKey  (event):
        input.set(input.get() + "4")
def FiveKey  (event):
        input.set(input.get() + "5")
def SixKey   (event):
        input.set(input.get() + "6")
def SevenKey (event):
        input.set(input.get() + "7")
def EightKey (event):
        input.set(input.get() + "8")
def NineKey  (event):
        input.set(input.get() + "9")
def ResetKey (event):
    input.set("")
def AddKey   (event):
        input.set(input.get() + "+")
def SubKey   (event):
        input.set(input.get() + "-")
def MultKey  (event):
        input.set(input.get() + "*")
def DivKey   (event):
        input.set(input.get() + "/")

def Unbind   (event):
        root.bind("1","")
        root.bind("2","")
        root.bind("3","")
        root.bind("4","")
        root.bind("5","")
        root.bind("6","")
        root.bind("7","")
        root.bind("8","")
        root.bind("9","")
        root.bind("<BackSpace>","")
        root.bind("+","" )
        root.bind("-","" )
        root.bind("*","" )
        root.bind("/","" )

def Bind  (event):
        root.bind("1", OneKey)
        root.bind("2", TwoKey)
        root.bind("3", ThreeKey)
        root.bind("4", FourKey)
        root.bind("5", FiveKey)
        root.bind("6", SixKey)
        root.bind("7", SevenKey)
        root.bind("8", EightKey)
        root.bind("9", NineKey)
        root.bind("<BackSpace>", ResetKey)
        root.bind("+", AddKey)
        root.bind("-", SubKey)
        root.bind("*", MultKey)
        root.bind("/", DivKey)



#Labels
lb_1=ttk.Label(frm, text="Calculadora",font=("Arial Black",25,"italic"),anchor="center",background="red")
lb_2=ttk.Label(frm, textvariable=output, anchor="center")

#Entries
ent_1=ttk.Entry(frm, textvariable=input)

#Buttons
bt_1=ttk.Button(frm,text="1",command=One)
bt_2=ttk.Button(frm,text="2",command=Two)
bt_3=ttk.Button(frm,text="3",command=Three)
bt_4=ttk.Button(frm,text="4",command=Four)
bt_5=ttk.Button(frm,text="5",command=Five)
bt_6=ttk.Button(frm,text="6",command=Six)
bt_7=ttk.Button(frm,text="7",command=Seven)
bt_8=ttk.Button(frm,text="8",command=Eight)
bt_9=ttk.Button(frm,text="9",command=Nine)
bt_0=ttk.Button(frm,text="0",command=Zero)
bt_reset=ttk.Button(frm,text="Reset",command=Reset)
bt_add=ttk.Button(frm,text="+",command=Add)
bt_sub=ttk.Button(frm,text="-",command=Sub)
bt_mult=ttk.Button(frm,text="*",command=Mult)
bt_div=ttk.Button(frm,text="/",command=Div)
bt_calculate=ttk.Button(frm,text="Calcular",command=Compute)
bt_mais_funcoes=ttk.Button(frm, text="+funções", command=MoreFunc)

#Configuração de widgets
root.bind("1",OneKey)
root.bind("2",TwoKey)
root.bind("3",ThreeKey)
root.bind("4",FourKey)
root.bind("5",FiveKey)
root.bind("6",SixKey)
root.bind("7",SevenKey)
root.bind("8",EightKey)
root.bind("9",NineKey)
root.bind("<BackSpace>",ResetKey)
root.bind("+",AddKey)
root.bind("-",SubKey)
root.bind("*",MultKey)
root.bind("/",DivKey)
ent_1.bind("<FocusIn>",Unbind)
ent_1.bind("<FocusOut>",Bind)



#Grid
frm.grid(sticky="news",column=0,row=0)
lb_1.grid(row=0,column=0,sticky="nwes",columnspan=4)
lb_2.grid(row=1,column=0, sticky="nwes",columnspan=4)
ent_1.grid(row=2,column=0,sticky="nwes",columnspan=4)

bt_1.grid(row=3, column=0,sticky="news")
bt_2.grid(row=3, column=1,sticky="news")
bt_3.grid(row=3, column=2,sticky="news")
bt_4.grid(row=4, column=0,sticky="news")
bt_5.grid(row=4, column=1,sticky="news")
bt_6.grid(row=4, column=2,sticky="news")
bt_7.grid(row=5, column=0,sticky="news")
bt_8.grid(row=5, column=1,sticky="news")
bt_9.grid(row=5, column=2,sticky="news")
bt_0.grid(row=6, column=0, sticky="news", columnspan=3)
bt_reset.grid(row=7, column=0, sticky="news",columnspan=3)
bt_add.grid(column=3,row=4,sticky="news")
bt_sub.grid(column=3,row=5,sticky="news")
bt_mult.grid(column=3,row=6,sticky="news")
bt_div.grid(column=3,row=7,sticky="news")
bt_calculate.grid(column=0,row=8,columnspan=4, sticky="news")
bt_mais_funcoes.grid(column=3, row=3, sticky="news")


#Configuração de grid
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
frm.grid_columnconfigure(0,weight=1)
frm.grid_columnconfigure(1,weight=1)
frm.grid_columnconfigure(2,weight=1)
frm.grid_columnconfigure(3,weight=1)
frm.grid_rowconfigure(0,weight=2)
frm.grid_rowconfigure(1,weight=2)
frm.grid_rowconfigure(2,weight=0)
frm.grid_rowconfigure(3,weight=0)
frm.grid_rowconfigure(4,weight=0)
frm.grid_rowconfigure(5,weight=0)
frm.grid_rowconfigure(6,weight=0)

#Mainloop da Janela
print(frm.grid_size())
print(root.grid_size())
print(lb_1.grid_info())
print(type(root.winfo_height()))
root.mainloop()
