import spacy

try:
    spacy.load("de_core_news_sm")
except:
    spacy.cli.download("de_core_news_sm")
