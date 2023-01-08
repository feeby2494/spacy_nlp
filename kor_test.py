import spacy
from spacy import displacy

nlp = spacy.load("ko_core_news_sm")

with open("data/kor_엿가락처.txt", "r") as f:
	text = f.read()

doc = nlp(text)

displacy.serve(doc, style="dep")
