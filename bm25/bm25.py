import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Handle empty corpus
    if len(docs) == 0:
        return np.array([])

    N = len(docs)

    # Deduplicate query terms while preserving order
    query_tokens = list(dict.fromkeys(query_tokens))

    # Document lengths
    doc_lens = np.array([len(doc) for doc in docs])
    avgdl = np.mean(doc_lens)

    # Term frequencies per document
    tf_docs = [Counter(doc) for doc in docs]

    # Document frequency
    df = Counter()
    for doc in docs:
        for word in set(doc):
            df[word] += 1

    scores = np.zeros(N)

    # BM25 scoring
    for term in query_tokens:

        df_t = df.get(term, 0)

        # If term never appears
        if df_t == 0:
            continue

        # IDF
        idf = math.log((N - df_t + 0.5) / (df_t + 0.5) + 1)

        for i in range(N):

            tf = tf_docs[i].get(term, 0)
            dl = doc_lens[i]

            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * dl / avgdl)

            scores[i] += idf * (numerator / denominator)

    return scores