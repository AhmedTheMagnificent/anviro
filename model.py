from transformers import pipeline

class MODEL:
    def __init__(self):
        self.ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
        # self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def prompt(self, text):
        ner_output = self.ner(text)
        output = {"entities": [], "tags": []}
        for ent in ner_output:
            
            output["entities"].append(ent["word"])
        return output