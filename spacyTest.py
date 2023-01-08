import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", "r") as f:
	text = f.read()

doc = nlp(text)

sentence1 = list(doc.sents)[0]
print(sentence1)

token2 = sentence1[2]
print(token2)

print(f"text: {token2.text}\nhead: {token2.head}\nLeft Edge: {token2.left_edge}\nRight Edge: {token2.right_edge}")

print(f"Entity Type INT: {token2.ent_type}\nEntity Type: {token2.ent_type_}")
print(f"Ent IOB: {token2.ent_iob_}\nLemma: {token2.lemma_}")
print(f"Morph : {token2.morph}\nPart of Speech: {token2.pos_}\nSyntactic Dependency: {token2.dep_}\nLanguage: {token2.lang_}")


displacy.render(sentence1, style="dep")

for ent in doc.ents:
	print(ent.text, ent.label_)

displacy.serve(doc, style="ent")
