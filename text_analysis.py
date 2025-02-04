from transformers import pipeline

# Initialize NER pipeline
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")

def analyze_long_text(text, chunk_size=100):
    descriptors = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        descriptors.extend(nlp(chunk))
    return descriptors

# Example usage
long_text = "Describe your long text here..."
descriptors = analyze_long_text(long_text)
print("Descriptors:", descriptors)
