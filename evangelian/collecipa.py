import collections
import string
import requests

def analyze_text(text):
    frequency = collections.Counter(text)
    total_chars = sum(frequency.values())
    num_words = len(text)
    num_unique_words = len(set(text))
    most_common_words = frequency.most_common(10)
    least_common_words = frequency.most_common()[:-11:-1]
    results = {
        'total_chars': total_chars,
        'num_words': num_words,
        'num_unique_words': num_unique_words,
        'most_common_words': most_common_words,
        'least_common_words': least_common_words
    }
    return results

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    stopwords = get_stopwords()
    words = [word for word in words if word not in stopwords]
    return words

def get_stopwords():
    url = 'https://www.textfixer.com/resources/common-english-words.txt'
    response = requests.get(url)
    stopwords = response.text.split()
    return stopwords

def main():
    url = 'https://www.gutenberg.org/files/11/11-0.txt'
    response = requests.get(url)
    text = response.text
    words = preprocess_text(text)
    results = analyze_text(words)
    print(results)

if __name__ == '__main__':
    main()
