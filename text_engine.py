import spacy
from sentence_transformers import SentenceTransformer, util

# Load spacy medium sized English language model
nlp = spacy.load("en_core_web_md")

# Optional custom stopwords to possibly enhance performance. Feel free to experiment with your own
custom_stopwords = ["a", "the", "it", "and", "if"]


def generate_ngrams(tokens, n):
    """
    Takes a list of tokens and an integer as arguments 
    and returns a list of ngrams generated from the input tokens.
    """
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]


def preprocess(text):
    """
    Tokenizes the text input and returns a list of normalized tokens 
    (in this case lowercased) while also excluding custom stopwords and punctuation.
    """
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if token.text.lower() not in custom_stopwords and not token.is_punct]
    return tokens


def analyze_text(input_text, terms, similarity_threshold=0.6):
    """
    Takes an input text, the list of standardized terms, and a similarity threshold as arguments.
    It preprocesses the input text by calling the preprocess function.
    It generates bigrams and trigrams, and combines them into a list called ngrams.
    It uses the model DistilBERT to encode the ngrams and the preloaded terms into embeddings,
    and then calculates cosine similarity scores using the encoded embeddings.
    """
    preprocessed_tokens = preprocess(input_text)

    bigram = generate_ngrams(preprocessed_tokens, 2)
    trigram = generate_ngrams(preprocessed_tokens, 3)
    ngrams = bigram + trigram

    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    ngram_embeddings = model.encode(ngrams, convert_to_tensor=True)
    terms_embeddings = model.encode(terms, convert_to_tensor=True)

    similarity_scores = util.pytorch_cos_sim(ngram_embeddings, terms_embeddings)

    suggestions = input_text
    for i, ngram in enumerate(ngrams):
        max_similarity = max(similarity_scores[i])
        if max_similarity >= similarity_threshold:
            index_of_max_similarity = similarity_scores[i].argmax()
            replacement = f"{{{ngram} <-> {terms[index_of_max_similarity]}}} (Similarity score: {max_similarity:.4f})"
            suggestions = suggestions.replace(ngram, replacement, 1)

    return suggestions


if __name__ == "__main__":
    # Preload standardized terms as a list
    preloaded_terms = ["Optimal performance", 
               "Utilise resources",
               "Enhance productivity",
               "Conduct an analysis",
               "Maintain a high standard",
               "Implement best practices",
               "Ensure compliance",
               "Streamline operations",
               "Foster innovation",
               "Drive growth",
               "Leverage synergies",
               "Demonstrate leadership",
               "Exercise due diligence",
               "Maximize stakeholder value",
               "Prioritise tasks",
               "Facilitate collaboration",
               "Monitor performance metrics",
               "Execute strategies",
               "Gauge effectiveness",
               "Champion change"]

    # User input
    user_input = input("\nEnter the text to analyze: ")

    # Specify a similarity threshold
    similarity_threshold = float(input("\nChoose a similarity threshold ranging from 0.0 to 1.0 (e.g. 0.6): "))

    # Analyze the text input with the specified threshold
    suggestions = analyze_text(user_input, preloaded_terms, similarity_threshold)

    # Print the results
    print("\nSuggestions:", "\n")
    print(suggestions)
