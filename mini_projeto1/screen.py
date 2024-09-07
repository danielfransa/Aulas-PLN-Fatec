from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from wordcloud import WordCloud
from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import matplotlib.pyplot as plt
import spacy
import nltk

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
      Label(self.frame_2, text="Nuvem de Palavras:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(relx=0.01, rely=0.0)
      self.canvas_nuvem = Canvas(self.frame_2, bg='white')
      self.canvas_nuvem.place(relx=0.03, rely=0.15, relwidth=0.94, relheight=0.80)

    def widgets_frame3(self):
      # Termos de busca e resultados
      Label(self.frame_3, text="Termos de Busca e Resultados:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(relx=0.01, rely=0.05)
      self.entry_termo_busca = Entry(self.frame_3, width=50)
      self.entry_termo_busca.place(relx=0.28, rely=0.05)
      self.btn_buscar = Button(self.frame_3, text="Buscar", font=('Arial', 10))
      self.btn_buscar.place(relx=0.7, rely=0.0)

      self.text_resultados = Text(self.frame_3)
      self.text_resultados.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.8)

    def widgets_frame4(self):
      # Resumo do texto
      Label(self.frame_4, text="Resumo do Texto:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(relx=0.01, rely=0.0)
      self.text_resumo = Text(self.frame_4)
      self.text_resumo.place(relx=0.03, rely=0.1, relwidth=0.94, relheight=0.90)

    def processar(self):
      url = self.entry_link.get()
      lang = self.lang_var.get()
      print(lang)
      print(url)

      # Seleciona a linguagem
      # nlp = spacy.load("en-core-web-md") if lang == 'ingles' else spacy.load("pt-core-news-md")
      token = 'english' if lang == 'ingles' else 'portuguese'

      g = Goose()
      self.article = g.extract(url)

      print(self.article.title)
      self.gerar_nuvem(self.article.cleaned_text)
      self.gerar_resumo(self.article.cleaned_text, token)

    def gerar_resumo(self, texto, token):
      nltk.download('punkt')
      #lista com as sentenças presentes no texto
      original_sentences = [sentence for sentence in nltk.sent_tokenize(texto)]

      #criando um texto pre-processado
      parser = PlaintextParser.from_string(texto, Tokenizer(token))

      #criando um objeto summarizer básico
      summarizer = SumBasicSummarizer()
      #criar o resumo (texto pre-processado, tamanho do resumo)
      sumary = summarizer(parser.document,len(original_sentences))

      #criando uma lista com as melhores sentenças do texto (sumary)
      best_sentences = []
      for sentence in sumary:
        best_sentences.append(sentence)

      resumo = []
      for i in best_sentences[:20]:
        resumo.append(i)

      self.text_resumo.delete('1.0', END)
      # Definir tags para formatação
      self.text_resumo.tag_configure('title', font=('Arial', 16, 'bold'))
      self.text_resumo.tag_configure('body', font=('Arial', 12))

      # Inserir o título com a tag 'title'
      self.text_resumo.insert('1.0', self.article.title + '\n\n', 'title')

      # Inserir o resumo com a tag 'body'
      self.text_resumo.insert(END, resumo, 'body')
 
    def gerar_nuvem(self, texto):
        
      # Gerando a nuvem de palavras
      wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)
      plt.figure(figsize=(10, 5))
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis('off')

      # Salvando e exibindo a nuvem de palavras
      plt.savefig("nuvem.png", format="png")
      imagem = Image.open("nuvem.png")
      imagem = imagem.resize((800, 150), Image.Resampling.LANCZOS)
      self.nuvem_img = ImageTk.PhotoImage(imagem)
      self.canvas_nuvem.create_image(0, 0, anchor=NW, image=self.nuvem_img)


Application()
