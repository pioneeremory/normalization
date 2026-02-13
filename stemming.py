"""
👨‍💻 Stemming Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Apply stemming using nltk.stem.PorterStemmer to reduce each word to its root form.
6️⃣ Print out the list of stemmed words.

📌 Hints:
- Remember to import the required NLTK modules.
- Think about what patterns to use in your regex for URLs and HTML tags.
- Inspect intermediate results to ensure your cleaning is working!

Write your code below this string.
"""

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# nltk.download('punkt')
# nltk.download('punkt_tab') 
# nltk.download('stopwords')

with open('story1.txt', 'r') as file:
    text_input = file.read()

# Step 2: Remove URLs and HTML tags using regex
text_cleaned = re.sub(r'http\S+|<.*?>', '', text_input)
# print(text_cleaned)

# Step 3: Remove hastags, asterisks, and excess punctuation

text_cleaned = re.sub(r'[#\*]', '', text_cleaned)
text_cleaned  = re.sub(r'[!?\.]{2,}', '', text_cleaned)
# print(text_cleaned)

# Step 4: Remove extra whitespace

text_cleaned = re.sub(r'\s+', ' ', text_cleaned).strip()
# print(text_cleaned)

# Step 5: Tokenize the text into words
tokens = word_tokenize(text_cleaned)
# print(tokens)

# Step 6: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
# print(filtered_tokens)

# Step 7: Apply stemming 
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in filtered_tokens]
print(stemmed_words)
