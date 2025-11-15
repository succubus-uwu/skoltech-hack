import spacy

nlp = spacy.load("ru_core_news_sm")
test_doc = nlp.make_doc(input())
for token in test_doc:
    print(f"'{token.text}' [{token.idx}:{token.idx + len(token.text)}]")