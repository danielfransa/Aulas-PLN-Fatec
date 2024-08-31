from tkinter import *

root = Tk()

# root.title("Mini Projeto - 1")
# root.configure(background='#1e3743')
# root.geometry("600x400")
# root.resizable(True, True)
# root.maxsize(width=1000, height=800)
# root.minsize(width=400, height=200)



# root.mainloop()


class Application():
  def __init__(self):
    self.root = root
    self.screen()
    self.frames()
    root.mainloop()

  def screen(self):
    self.root.title("Mini Projeto - 1")
    self.root.configure(background='#1e3743')
    self.root.geometry("1200x1000")
    self.root.resizable(True, True)
    #Deveria setar o tamanho máximo mas aparetemente não esta funcionando
    self.root.maxsize(width=1400, height=1200)
    #Deveria setar o tamanho minimo mas aparetemente não esta funcionando
    self.root.minsize(width=400, height=200)

  def frames(self):
    self.frame_1  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2, background='#D3D3D3')
    self.frame_1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.15)

    self.frame_2  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2, background='#D3D3D3')
    self.frame_2.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.22)

    self.frame_3  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2, background='#D3D3D3')
    self.frame_3.place(relx=0.03, rely=0.44, relwidth=0.94, relheight=0.22)

    self.frame_4  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2, background='#D3D3D3')
    self.frame_4.place(relx=0.03, rely=0.68, relwidth=0.94, relheight=0.3)



Application()

#cores
#3A697E