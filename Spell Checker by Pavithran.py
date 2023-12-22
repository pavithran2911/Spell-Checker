from textblob import TextBlob

def spell_check():
    while True:
        try:
            word_to_check = input("Enter the word to be checked (0 to exit): ")
            if word_to_check.lower() == '0':
                break

            print("Original text: " + word_to_check)

            # Correcting the text
            corrected_text = TextBlob(word_to_check).correct()

            # Prints the corrected spelling
            print("Corrected text: " + str(corrected_text))

            # Additional features: Sentiment analysis
            sentiment = TextBlob(corrected_text).sentiment
            print(f"Sentiment: Polarity = {sentiment.polarity}, Subjectivity = {sentiment.subjectivity}")

            # Provide more information about the corrected word
            correction_details = f"Correction details: {word_to_check} -> {corrected_text}"
            print(correction_details)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    spell_check()
