import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Input text
text = input("Enter text: ")

# 1. Convert to lowercase
text = text.lower()

# 2. Remove punctuation and special characters
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 3. Tokenization
tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)

# 4. Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]

print("\nAfter Stop Word Removal:")
print(filtered_words)

# 5. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nAfter Stemming:")
print(stemmed_words)