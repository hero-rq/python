import nltk

def generate_bigrams(text):
  tokens = nltk.word_tokenize(text)
  return nltk.bigrams(tokens)

text = input()
bigrams = generate_bigrams(text)

# Print the generated bigrams
for bigram in bigrams:
  print(bigram)
