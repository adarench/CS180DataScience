import argparse
import numpy as np

def tokenize_documents(documentsTxt):
    """Tokenize the input text into a list of words, making them lowercase."""
    documents = documentsTxt.strip().split('\n')
    tokenized_documents = [doc.lower().split(' ') for doc in documents]
    return tokenized_documents

def build_vocabulary(tokenized_documents):
    """Build a sorted list of unique words found in all documents."""
    vocabulary = sorted(set(word for document in tokenized_documents for word in document))
    return vocabulary

def construct_feature_matrix(tokenized_documents, vocabulary):
    """Construct the feature matrix using one-hot encoding for word occurrences."""
    vocab_index = {word: i for i, word in enumerate(vocabulary)}
    feature_matrix = np.zeros((len(tokenized_documents), len(vocabulary)), dtype=int)
    
    for doc_idx, document in enumerate(tokenized_documents):
        for word in document:
            if word in vocab_index:  # This check is technically redundant given the construction method of vocabulary
                feature_matrix[doc_idx, vocab_index[word]] += 1
                
    return feature_matrix

def main(documentsTxt):
    tokenized_documents = tokenize_documents(documentsTxt)
    vocabulary = build_vocabulary(tokenized_documents)
    feature_matrix = construct_feature_matrix(tokenized_documents, vocabulary)
    
    # For the purpose of matching the output format exactly as shown in the example,
    # we'll print the feature matrix without brackets and with spaces instead of commas.
    print("# Features:")
    for row in feature_matrix:
        print(' '.join(str(x) for x in row))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())
