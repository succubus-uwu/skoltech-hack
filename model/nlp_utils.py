import spacy

nlp = spacy.blank("ru")
test_doc = nlp.make_doc(input())
for token in test_doc:
    print(f"'{token.text}' [{token.idx}:{token.idx + len(token.text)}]")