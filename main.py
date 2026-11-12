# 1. Data Extraction 
from pypdf import PdfReader

# PDF file path
pdf_path = "stats interview questions-answers.pdf"

# Read PDF
reader = PdfReader(pdf_path)

# Extract text from all pages
text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

# Display extracted text
print("Total pages:", len(reader.pages))
print("Extracted text:")
print(text[:2000])

# Save extracted text
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("PDF text extracted successfully!")

# 2. Data Cleaning – Text clean 
import re

# Convert text to lowercase
clean_text = text.lower()

# Remove unwanted characters
clean_text = re.sub(r"[^a-z\s.]", " ", clean_text)

# Remove extra spaces
clean_text = re.sub(r"\s+", " ", clean_text)

# Split text into sentences
sentences = re.split(r"[.!?]+", clean_text)

# Remove empty sentences
sentences = [s.strip() for s in sentences if s.strip()]

# 3. Tokenization
# Tokenization
tokenized_sentences = [
    sentence.split() for sentence in sentences
]

print("Total sentences:", len(tokenized_sentences))
print("First 5 tokenized sentences:")
print(tokenized_sentences[:5])
from gensim.models import Word2Vec

# Train Word2Vec model
word2vec_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4,
    sg=1
)

print("Word2Vec model trained successfully!")

# Get vector for mean
word = "mean"

vector = word2vec_model.wv[word]

print("Word:", word)
print("Vector:", vector)
print("Vector Shape:", vector.shape)

# Find similar words
similar_words = word2vec_model.wv.most_similar(
    "mean", topn=5
)

print("Similar words:", similar_words)

# Save Word2Vec model
word2vec_model.save("statistics_word2vec.model")

# Save word vectors
word2vec_model.wv.save_word2vec_format(
    "statistics_word2vec.txt",
    binary=False
)
from staticvectors import StaticVectors
import numpy as np

# Load pre-trained GloVe model
glove_model = StaticVectors("neuml/glove-6B")

print("GloVe model loaded successfully!")

# Select words from Statistics PDF
words = [
    "mean",
    "median",
    "variance",
    "probability",
    "correlation",
    "statistics"
]

# Get GloVe embeddings
glove_embeddings = glove_model.embeddings(words)

print("GloVe Embeddings:")
print(glove_embeddings)

print("Embedding Shape:", glove_embeddings.shape)

# Save embeddings
np.save(
    "statistics_glove_embeddings.npy",
    glove_embeddings
)

print("GloVe embeddings saved successfully!")

# Verify Saved Files
import os

files = [
    "extracted_text.txt",
    "statistics_word2vec.model",
    "statistics_word2vec.txt",
    "statistics_glove_embeddings.npy"
]

print("Generated files:")

for file in files:
    if os.path.exists(file):
        print(file, "- Saved successfully")
    else:
        print(file, "- Not found")