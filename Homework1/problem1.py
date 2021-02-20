# Create the script ​problem1.py, ​which gets 
# 3 positional command line arguments of type String: ​
# text, first_word, second_word. ​
# Print the new version of the given ​text, 
# replacing all the occurrences of the ​first_word ​
# in ​text ​with the ​second_word ​in the following format:
# “The given text: This text is a sample text. ” “First word: text”
# “Second word: image”
# “Output string: This image is a sample image. ”

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', type=str)
parser.add_argument('first_word', type=str)
parser.add_argument('second_word', type = str)
args = parser.parse_args()

result = args.text.replace(args.first_word, args.second_word)

print("The given text: %s" %args.text)
print("First word: %s" %args.first_word)
print("Second word: %s" %args.second_word)
print("Output striing: %s" %result)