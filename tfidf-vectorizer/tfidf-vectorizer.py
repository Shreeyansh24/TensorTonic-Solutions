import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
     # Handle empty corpus
    if not documents:
        return np.zeros((0, 0)), []

    # Tokenize documents (lowercase + split)
    tokenized_docs = [doc.lower().split() for doc in documents]

    # Build vocabulary (sorted)
    vocab = sorted(set(word for doc in tokenized_docs for word in doc))
    vocab_size = len(vocab)
    n_docs = len(documents)

    # Handle case where all documents are empty
    if vocab_size == 0:
        return np.zeros((n_docs, 0)), []

    # Word → index mapping
    word_to_idx = {word: i for i, word in enumerate(vocab)}

    # Initialize TF matrix
    tf = np.zeros((n_docs, vocab_size))

    # Compute TF
    for d_idx, doc in enumerate(tokenized_docs):
        if len(doc) == 0:
            continue

        counts = Counter(doc)
        total_terms = len(doc)

        for word, count in counts.items():
            tf[d_idx, word_to_idx[word]] = count / total_terms

    # Compute DF (document frequency)
    df = Counter()
    for doc in tokenized_docs:
        for word in set(doc):
            df[word] += 1

    # Compute IDF
    idf = np.zeros(vocab_size)
    for word, idx in word_to_idx.items():
        idf[idx] = math.log(n_docs / df[word])

    # TF-IDF
    tfidf_matrix = tf * idf

    return tfidf_matrix, vocab