from transformers import pipeline

# Use a pre-trained NLP model for entity recognition
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

description = "A tall man with brown hair and a scar on his cheek."
features = nlp(description)

print(features)  # This will print entities like 'hair', 'height', etc.
