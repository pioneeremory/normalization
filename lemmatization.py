"""
👨‍💻 Lemmatization Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Tag each word with its part of speech using nltk.pos_tag.
6️⃣ Map POS tags to WordNet tags so the lemmatizer can use them.
7️⃣ Apply lemmatization using nltk.stem.WordNetLemmatizer, passing the correct POS.
8️⃣ Print out the list of lemmatized words.

📌 Hints:
- You’ll need a helper function to convert Treebank POS tags to WordNet POS tags.
- Check your intermediate outputs (POS tags, lemmatized results).

Write your code below this string.
"""
import re
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun if unknown

with open('story2.txt', 'r') as file:
    text_input = file.read()

# 3. Regex Noise Removal
text_input = re.sub(r'<[^>]+>', '', text_input)  # HTML tags
text_input = re.sub(r'https?://\S+|www\.\S+', '', text_input)  # URLs
text_input = re.sub(r'[#\*]', '', text_input)  # Hashtags and asterisks
text_input = re.sub(r'[!?\.]{2,}', '', text_input)  # Excessive punctuation
clean_text = re.sub(r'\s+', ' ', text_input).strip() # Extra whitespace

tokens = word_tokenize(clean_text)

stop_words = set(stopwords.words('english'))
stopwords_removed = [w for w in tokens if w.lower() not in stop_words]

tagged_words = pos_tag(stopwords_removed)

print(tagged_words)

lemmatized_words_with_pos = [
    lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag))
    for word, pos_tag in tagged_words
]

print(lemmatized_words_with_pos)