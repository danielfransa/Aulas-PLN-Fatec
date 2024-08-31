import spacy

nlp = spacy.load("pt_core_news_sm")

def identificar_verbos(frase):
    doc = nlp(frase)
    verbos = [token.text for token in doc if token.pos_ == "VERB"]
    return verbos

frase = "Hoje vamos aprender bastante."

verbos_encontrados = identificar_verbos(frase)

print(f"Verbos encontrados: {verbos_encontrados}")
print(f"Quantidade de verbos: {len(verbos_encontrados)}")