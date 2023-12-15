## Text Improvement Engine
*NLP tool to analyze a given text and suggest improvements based on the semantic similarity to a list of standardized terms*

This tool leverages natural language processing (NLP) and semantic similarity to analyze a given text and provide suggestions for improvements based on a list of standardized terms. 
The goal is to align the input text with the standardized terms from the list, which represent the ideal expression of certain concepts. These standardized terms represent the ideal way certain concepts should be articulated, and this tool recommends changes to align the input text closer to these standards.

<br>

### Features

Tokenization and preprocessing of the input text, including the removal of optional custom stopwords and punctuation.

Generates ngrams (in this case bigrams and trigrams) from the preprocessed tokens to capture meaningful combinations of words.

Encodes the ngrams extracted from the input text and the preloaded list of standardized terms. The tool calculates cosine similarity scores between the embeddings.

Recommends improvements to the input text by identifying ngrams with high similarity scores to the standardized terms. Suggestions include replacements with corresponding standardized terms, their similarity scores, and a visual representation of the matching terms.

<br>

### Technologies Used

This tool uses the spaCy library and its medium sized English language model. This library was chosen because of its ease of use, efficiency, and it was designed specifically for production use and development of applications.
The medium sized English language model was chosen for convenience because it contains word vectors at a modest download size (about 40MB) while maintaining great performance, as opposed to the large model which has a significantly larger download size or the small model which has no vectors.

It also uses the DistilBERT model through the Sentence Transformers library to generate embeddings for sentences. It was chosen because it is a good compromise between model size and accuracy. It retains 95% of BERT’s performance while being computationally more efficient and easier to deploy.

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

- Enter the text you want to analyze when prompted:

  ![example_00](https://github.com/rodjoost/text_improvement_engine/assets/66536020/77be5dee-1673-4070-be9d-86e0c419f148)

  
- Choose a similarity threshold (between 0.0 and 1.0) to control the sensitivity of the suggestions:

  ![example_02](https://github.com/rodjoost/text_improvement_engine/assets/66536020/c6e9ab7a-3fa8-4bdd-a7a1-df58b6a8bdaa)


- Results: The tool will output the input text with suggested improvements based on the similarity to the standardized terms:

  ![example_03](https://github.com/rodjoost/text_improvement_engine/assets/66536020/12efb18c-aa33-4d45-83be-82442ecf8f31)


<br>

##### Customize:

- Custom stopwords: You can experiment with your own custom stopwords for better performance by adding and/or removing words to the custom_stopwords list.

- Standardized terms: Modify the preloaded_terms list with your own set of standardized terms to tailor the tool to your specific requirements.

Feel free to experiment with different texts, thresholds, and customization options to enhance the tool's performance for your specific use case.

<br>

### The Future

Implementation for sentiment analysis and lemmatization, among other features, are planned for future releases in order to keep improving the tool's performance.
