#입력된 문자를 2-gram 방식으로 출력 
#2-gram 방식이란 문자열에서 2개의 연속된 요소를 나눠서 출력하는 방법 
text = input()
text += ''
for i in range(0, len(text)-1):
  print(text[i]+text[i+1],'\n')
  
'''
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
