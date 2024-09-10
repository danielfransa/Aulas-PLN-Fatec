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
from spacy.matcher import PhraseMatcher
 
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
    self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
    self.frame_1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.15)

    # Frame 2: Nuvem de palavras
    self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
    self.frame_2.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.22)

    # Frame 3: Termos de busca
    self.frame_3 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
    self.frame_3.place(relx=0.03, rely=0.44, relwidth=0.94, relheight=0.22)

    # Frame 4: Resumo do texto
    self.frame_4 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
    self.frame_4.place(relx=0.03, rely=0.68, relwidth=0.94, relheight=0.3)

  def widgets_frame1(self):
    # Título e instruções
    Label(self.frame_1, text="Escolha a linguagem e insira o link ou termo de interesse:", bg='#dfe3ee', font=('Arial', 12, 'bold')).place(relx=0.25, rely=0.0)

    # Entrada para o link ou termo
    Label(self.frame_1, text="Link/Termo:", bg='#dfe3ee', font=('Arial', 10)).place(relx=0.01, rely=0.3)
    self.entry_link = Entry(self.frame_1, width=90)
    self.entry_link.place(relx=0.1, rely=0.3)

    # Opção de idioma
    Label(self.frame_1, text="Idioma:", bg='#dfe3ee', font=('Arial', 10)).place(relx=0.01, rely=0.5)
    self.lang_var = StringVar(value='portugues')
    Radiobutton(self.frame_1, text="Português", variable=self.lang_var, value='portugues', bg='#dfe3ee').place(relx=0.1, rely=0.5)
    Radiobutton(self.frame_1, text="Inglês", variable=self.lang_var, value='ingles', bg='#dfe3ee').place(relx=0.2, rely=0.5)

    # Quantidade de frases no Resumo
    Label(self.frame_1, text="Escolha a quantidade de frases para o resumo:", bg='#dfe3ee', font=('Arial', 10)).place(relx=0.01, rely=0.75)
    self.entry_number = Entry(self.frame_1, width=4)
    self.entry_number.place(relx=0.30, rely=0.75)

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
    # Aqui está a modificação para vincular o botão à função buscar_termos
    self.btn_buscar = Button(self.frame_3, text="Buscar", font=('Arial', 10), command=self.buscar_termos)
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
    token = 'english' if lang == 'ingles' else 'portuguese'

    g = Goose()
    self.article = g.extract(url)

    print(self.article.title)
    self.gerar_nuvem(self.article.cleaned_text)
    self.gerar_resumo(self.article.cleaned_text, token)

  def gerar_resumo(self, texto, token):
    nltk.download('punkt')
    original_sentences = [sentence for sentence in nltk.sent_tokenize(texto)]

    parser = PlaintextParser.from_string(texto, Tokenizer(token))
    summarizer = SumBasicSummarizer()
    sumary = summarizer(parser.document, len(original_sentences))

    best_sentences = [str(sentence) for sentence in sumary]

    self.text_resumo.delete('1.0', END)
    self.text_resumo.tag_configure('title', font=('Arial', 16, 'bold'))
    self.text_resumo.tag_configure('body', font=('Arial', 12))

    self.text_resumo.insert('1.0', self.article.title + '\n\n', 'title')

    num_sentences = int(self.entry_number.get())

    for resumo in best_sentences[:num_sentences]:
      self.text_resumo.insert(END, '- ' + resumo + '\n', 'body')

  def gerar_nuvem(self, texto):
    nlp = spacy.load("en_core_web_md") if self.lang_var.get() == 'ingles' else spacy.load("pt_core_news_md")
    cleaned_text = self.preprocessing(texto, nlp)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    plt.savefig("nuvem.png", format="png")
    imagem = Image.open("nuvem.png")
    imagem = imagem.resize((800, 150), Image.Resampling.LANCZOS)
    self.nuvem_img = ImageTk.PhotoImage(imagem)
    self.canvas_nuvem.create_image(0, 0, anchor=NW, image=self.nuvem_img)

  def buscar_termos(self):
    termo = self.entry_termo_busca.get()
    nlp = spacy.load("en_core_web_md") if self.lang_var.get() == 'ingles' else spacy.load("pt_core_news_md")
    cleaned_text = self.preprocessing(self.article.cleaned_text, nlp)

    search_strings = [termo]
    tokens_list = [nlp(item) for item in search_strings]

    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('SEARCH', None, *tokens_list)

    document = nlp(cleaned_text)
    matches = matcher(document)

    self.text_resultados.delete('1.0', END)
    self.text_resultados.insert(END, f'Número de correspondências: {len(matches)}\n\n')

    number_of_words = 3

    for i in matches:
      start = i[1] - number_of_words  # Posição inicial do contexto da palavra
      if start < 0:
          start = 0

      # Para cada termo encontrado, crie a frase contextual
      surrounding_text = str(document[start:i[2] + number_of_words])

      # Insira o texto da frase no widget `Text`
      self.text_resultados.insert(END, surrounding_text + '\n\n')

      # Calcule a posição do termo encontrado dentro da frase atual
      start_idx = self.text_resultados.search(termo, END, backwards=True)  # Use a função `search` do Tkinter para encontrar a palavra
      end_idx = f"{start_idx}+{len(termo)}c"  # Calcula o índice final da palavra a ser destacada

      # Adiciona a tag para destacar o termo
      self.text_resultados.tag_add('highlight', start_idx, end_idx)
      self.text_resultados.tag_config('highlight', background='yellow', foreground='black')

    

  def preprocessing(self, sentence: str, nlp) -> str:
    sentence = sentence.lower()
    sentence = sentence.replace('.', ' ')
    sentence = sentence.replace('[', ' ')
    sentence = sentence.replace(']', ' ')
    tokens = [token.text for token in nlp(sentence) if not (token.is_stop or token.like_num or token.is_punct or token.is_space or len(token) == 1)]
    tokens = ' '.join(tokens)
    return tokens
 
 
Application()