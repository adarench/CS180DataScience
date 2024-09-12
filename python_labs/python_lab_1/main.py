import json
import string
import argparse
import os

def count_words(input_string):
    # Debug: Print the received input string
    print("Processing string:", input_string)

    # Remove punctuation and make lowercase
    translator = str.maketrans('', '', string.punctuation)
    processed_string = input_string.translate(translator).lower()

    # Tokenize the string
    words = processed_string.split()

    # Count words using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Debug: Print the word counts
    print("Word counts:", word_counts)

    return word_counts

# Set up argument parsing
parser = argparse.ArgumentParser(description="Word Count Program")
parser.add_argument("--string", type=str, help="string to analyze")
args = parser.parse_args()

# Call the word counting function
word_counts = count_words(args.string)

# Debugging: Print current working directory
print("Current Working Directory:", os.getcwd())

# Write the result to a JSON file
with open("word-counts.json", "w") as file:
    json.dump(word_counts, file)

# Debugging: Confirm file writing
print("Word count written to word-counts.json")
