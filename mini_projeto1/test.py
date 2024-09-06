from tkinter import *
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.screen()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()
        self.widgets_frame4()
        root.mainloop()

    def screen(self):
        self.root.title("Mini Projeto - 1")
        self.root.configure(background='#1e3743')
        self.root.geometry("1200x1000")
        self.root.resizable(True, True)
        self.root.maxsize(width=1400, height=1200)
        self.root.minsize(width=400, height=200)

    def frames(self):
        # Frame 1: Entrada do usuário
        self.frame_1  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.15)

        # Frame 2: Nuvem de palavras
        self.frame_2  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.22)

        # Frame 3: Termos de busca
        self.frame_3  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_3.place(relx=0.03, rely=0.44, relwidth=0.94, relheight=0.22)

        # Frame 4: Resumo do texto
        self.frame_4  = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_4.place(relx=0.03, rely=0.68, relwidth=0.94, relheight=0.3)

    def widgets_frame1(self):
        # Título e instruções
        Label(self.frame_1, text="Escolha a linguagem e insira o link ou termo de interesse:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(relx=0.25, rely=0.0)

        # Entrada para o link ou termo
        Label(self.frame_1, text="Link/Termo:", bg='#dfe3ee', font=('Arial', 10)).place(relx=0.01, rely=0.3)
        self.entry_link = Entry(self.frame_1, width=90)
        self.entry_link.place(relx=0.1, rely=0.3)

        # Opção de idioma
        Label(self.frame_1, text="Idioma:", bg='#dfe3ee', font=('Arial', 10)).place(relx=0.01, rely=0.6)
        self.lang_var = StringVar(value='portugues')
        Radiobutton(self.frame_1, text="Português", variable=self.lang_var, value='portugues', bg='#dfe3ee').place(relx=0.1, rely=0.6)
        Radiobutton(self.frame_1, text="Inglês", variable=self.lang_var, value='ingles', bg='#dfe3ee').place(relx=0.2, rely=0.6)

        # Botão de processar
        self.btn_processar = Button(self.frame_1, text="Processar", font=('Arial', 10), command=self.processar)
        self.btn_processar.place(relx=0.9, rely=0.65)

    def widgets_frame2(self):
        # Nuvem de palavras
        Label(self.frame_2, text="Nuvem de Palavras:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(x=10, y=10)
        self.canvas_nuvem = Canvas(self.frame_2, bg='white', width=800, height=150)
        self.canvas_nuvem.place(relx=0.03, rely=0.3)

    def widgets_frame3(self):
        # Termos de busca e resultados
        Label(self.frame_3, text="Termos de Busca e Resultados:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(x=10, y=10)
        self.entry_termo_busca = Entry(self.frame_3, width=30)
        self.entry_termo_busca.place(x=200, y=50)
        self.btn_buscar = Button(self.frame_3, text="Buscar", font=('Arial', 10))
        self.btn_buscar.place(x=400, y=50)

        self.text_resultados = Text(self.frame_3, height=5, width=80)
        self.text_resultados.place(relx=0.03, rely=0.4)

    def widgets_frame4(self):
        # Resumo do texto
        Label(self.frame_4, text="Resumo do Texto:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(x=10, y=10)
        self.text_resumo = Text(self.frame_4, height=10, width=100)
        self.text_resumo.place(relx=0.03, rely=0.2)

    def processar(self):
        print(self.entry_link)
        pass


Application()
