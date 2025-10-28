from model import MODEL

def main():
    ner = MODEL()
    text = input("\nEnter text: ")
    output = ner.prompt(text)
    print("\nRaw Output:\n", output)


if __name__ == "__main__":
    main()