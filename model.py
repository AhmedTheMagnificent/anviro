from transformers import pipeline

class MODEL:
    def __init__(self):
        self.ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
        self.summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

    def prompt(self, text):
        ner_output = self.ner(text)
        entities = [ent["word"] for ent in ner_output]
        return entities
    
    def summarize(self, text):
        summary = self.summarizer(text, max_length=30, min_length=10, do_sample=False)[0]["summary_text"]
        tags = summary.strip()
        return tags
    
    def analyze(self, text):
        return {"entities": self.prompt(text), "tags": self.summarize(text)}
    
    
# model = MODEL()

# inp = input("enter text: ")
# print(model.analyze(inp))