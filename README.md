## Text Improvement Engine
*NLP tool to analyze a given text and suggest improvements based on the semantic similarity to a list of standardized terms*

This tool leverages natural language processing (NLP) and semantic similarity to analyze a given text and provide suggestions for improvements based on a list of standardized terms. 
The goal is to align the input text with the standardized terms from the list, which represent the ideal expression of certain concepts. These standardized terms represent the ideal way certain concepts should be articulated, and this tool recommends changes to align the input text closer to these standards.

<br>

### Features

Tokenization and preprocessing of the input text, including the removal of optional custom stopwords and punctuation.

Generates ngrams (in this case bigrams and trigrams) from the preprocessed tokens to capture meaningful combinations of words.

Encodes the ngrams extracted from the input text and the preloaded list of standardized terms. The tool calculates cosine similarity scores between the embeddings.

Recommends improvements to the input text by identifying ngrams with high similarity scores to the standardized terms. Suggestions include replacements with corresponding standardized terms, similarity scores, and a visual representation of the matching terms.

<br>

### Technologies Used

This tool uses the spaCy library and its medium sized English language model. This library was chosen because of its easy of use, efficiency, and it's designed specifically for production use and development of applications.
The medium sized English language model was chosen for convenience because it contains word vectors at a modest size (about 40MB) while maintaining great performance, as opposed to the large model which has a significantly larger size or the small model which has no vectors.

It also uses the DistilBERT model through the Sentence Transformers library for generating embeddings for sentences. It was chosen because it is a good compromise between model size and accuracy. It retains 95% of BERT’s performance while being computationally more efficient and easier to deploy.

<br>

### How to Use

##### Install Dependencies:

    pip install spacy

    pip install sentence_transformers

    pip install torch

##### Download SpaCy medium sized English model:

    python -m spacy download en_core_web_md


##### Run the Tool:

    python text_engine.py

- Enter the text you want to analyze when prompted.
- Choose a similarity threshold (between 0.0 and 1.0) to control the sensitivity of the suggestions.

- Results: The tool will output the input text with suggested improvements based on the similarity to the standardized phrases.

<br>

##### Customize:

- Custom Stopwords: You can experiment with your own custom stopwords for better performance by adding and/or removing words to the custom_stopwords list.

- Standardized terms: Modify the preloaded_terms list with your own set of standardized terms to tailor the tool to your specific requirements.

Feel free to experiment with different texts, thresholds, and customization options to enhance the tool's performance for your specific use case.

<br>

### The Future

Implementation for sentiment analysis and lemmatization, among other features, are planned for future releases in order to keep improving the tool's performance.
