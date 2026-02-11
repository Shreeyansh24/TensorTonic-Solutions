import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    if not documents:
        return np.zeros((0,0)),[]
    tok_doc=[doc.lower().split() for doc in documents]
    vocab=sorted(set(words for doc in tok_doc for words in doc))
    vocab_size=len(vocab)
    n_doc=len(documents)
    if vocab_size == 0:
        return np.zeros((n_docs, 0)), []
    word_to_idx = {word: i for i, word in enumerate(vocab)}
    tf = np.zeros((n_doc, vocab_size))
    for d_idx, doc in enumerate(tok_doc):
        if len(doc) == 0:
            continue

        counts = Counter(doc)
        total_terms = len(doc)

        for word, count in counts.items():
            tf[d_idx, word_to_idx[word]] = count / total_terms
    df = Counter()
    for doc in tok_doc:
        for word in set(doc):
            df[word] += 1

    # Compute IDF
    idf = np.zeros(vocab_size)
    for word, idx in word_to_idx.items():
        idf[idx] = math.log(n_doc / df[word])

    # TF-IDF
    tfidf_matrix = tf * idf

    return tfidf_matrix, vocab