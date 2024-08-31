import spacy
from spacy import displacy

nlp = spacy.load("pt_core_news_sm")

def substituir_nomes_proprios(texto):
  doc = nlp(texto)
  texto_alterado = []

  for token in doc:
    if token.ent_type_ == "PER":
      texto_alterado.append("XXXX")
    else:
      texto_alterado.append(token.text)
  
  return " ".join(texto_alterado)

texto = input("Digite um texto em português: ")

texto_modificado = substituir_nomes_proprios(texto)

print(f"Texto alterado: {texto_modificado}")

doc_modificado = nlp(texto_modificado)
displacy.serve(doc_modificado, style="dep")
