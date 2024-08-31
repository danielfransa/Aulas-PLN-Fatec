import spacy
import en_core_web_sm
import nltk
from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer



nlp=spacy.load('en_core_web_sm')
nltk.download('punkt')
nltk.download('punkt_tab')

url = input("Por favor, insira a URL do artigo em inglês: ")

g=Goose()
article=g.extract(url)

# article.cleaned_text

original_sentences = [sentence for sentence in nltk.sent_tokenize(article.cleaned_text)]

total_sentences = len(original_sentences)

# original_sentences

parser = PlaintextParser.from_string(article.cleaned_text, Tokenizer('english'))


summarizer = SumBasicSummarizer()

sumary = summarizer(parser.document, total_sentences)

best_sentences = []
for sentence in sumary:
  best_sentences.append(sentence)


num_sentences = int(input("Por favor, insira o número de sentenças a exibir: "))

# Garantir que o número não seja maior que o tamanho de 'best_sentences'
num_sentences = min(num_sentences, len(best_sentences))


print(f"Sumário - {article.title}")
for i in best_sentences[:10]:
    print(f"- {i}")