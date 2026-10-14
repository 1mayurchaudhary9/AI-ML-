import re
from collections import Counter, defaultdict

# Training corpus
text = """
Artificial Intelligence is transforming industries.
Artificial Intelligence is changing the world.
Artificial Intelligence is a powerful technology.
"""

# 1. Convert text to lowercase
text = text.lower()

# 2. Tokenize the text
words = re.findall(r'\b[a-z]+\b', text)

# 3. Generate bigrams
bigrams = list(zip(words, words[1:]))

# 4. Count frequency of each bigram
bigram_counts = Counter(bigrams)

print("Bigrams and their frequencies:")
for bigram, count in bigram_counts.items():
    print(bigram, ":", count)

# 5. Store possible next words
next_words = defaultdict(Counter)

for word1, word2 in bigrams:
    next_words[word1][word2] += 1

# 6. Accept input word
word = input("\nEnter a word: ").lower()

# 7. Predict most frequent next word
if word in next_words:
    predicted_word = next_words[word].most_common(1)[0][0]
    print("Predicted next word:", predicted_word)
else:
    print("No prediction available for this word.")