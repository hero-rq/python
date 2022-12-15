'''
text = input()
text += ''
for i in range(0, len(text)-1):
  print(text[i]+text[i+1],'\n')
  
import nltk

def generate_bigrams(text):
  tokens = nltk.word_tokenize(text)
  return nltk.bigrams(tokens)

text = input()
bigrams = generate_bigrams(text)

# Print the generated bigrams
for bigram in bigrams:
  print(bigram)
'''
s = input()
p = ''

for i in range(0, len(s)):
  if s[i] >= 'A' and s[i] <= 'Z':
    p += s[i]
  else:
    pass

print(p)
