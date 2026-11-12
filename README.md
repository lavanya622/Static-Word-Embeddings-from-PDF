# Static Word Embeddings from PDF

## 📌 Project Overview

This project demonstrates how to extract text from a PDF document and generate static word embeddings using **Word2Vec** and **GloVe**.

A Statistics Interview Questions and Answers PDF is used as the input dataset. The extracted text is cleaned, split into sentences, and tokenized before training a Word2Vec model. Pre-trained GloVe embeddings are also used to generate vector representations for selected statistical terms.

## 🎯 Objectives

- Extract text from a PDF document.
- Clean and preprocess the extracted text.
- Split text into sentences and tokenize words.
- Train a Word2Vec model using the extracted text.
- Generate word vectors for selected words.
- Find semantically similar words using Word2Vec.
- Load pre-trained GloVe embeddings.
- Generate and save word embeddings.

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- PyPDF
- Regular Expressions
- NumPy
- Gensim
- StaticVectors
- Word2Vec
- GloVe

## 📂 Project Structure

```text
Static-Word-Embeddings-from-PDF/
│
├── main.py
├── Statistics_Word_Embeddings.ipynb
├── stats interview questions-answers.pdf
├── extracted_text.txt
├── statistics_word2vec.model
├── statistics_word2vec.txt
├── statistics_glove_embeddings.npy
├── requirements.txt
└── README.md
```

## ⚙️ Project Workflow

### 1. PDF Text Extraction

- Used `PdfReader` from the `pypdf` library.
- Extracted text from all pages of the Statistics Interview Questions PDF.
- Saved the extracted content into `extracted_text.txt`.

### 2. Text Cleaning

- Converted text into lowercase.
- Removed unwanted characters using regular expressions.
- Removed extra spaces.
- Split the cleaned text into sentences.

### 3. Tokenization

- Split each sentence into individual words.
- Created tokenized sentences for Word2Vec training.

### 4. Word2Vec Model Training

- Used the Gensim library to train a Word2Vec model.
- Applied the Skip-gram (`sg=1`) architecture.
- Generated 100-dimensional word vectors.

**Model Parameters:**

| Parameter | Value |
|---|---|
| Vector Size | 100 |
| Window Size | 5 |
| Minimum Count | 1 |
| Workers | 4 |
| Architecture | Skip-gram |

### 5. Word Vector Extraction

- Extracted the vector representation of the word `mean`.
- Checked the shape of the generated vector.
- Obtained a 100-dimensional vector.

### 6. Similar Word Identification

- Used `most_similar()` to identify words similar to `mean`.
- Displayed the top 5 similar words based on cosine similarity.

### 7. Saving Word2Vec Model

Saved the trained Word2Vec model and word vectors in:

- `statistics_word2vec.model`
- `statistics_word2vec.txt`

### 8. GloVe Embeddings

- Loaded pre-trained GloVe embeddings using the `StaticVectors` library.
- Selected six statistical terms:

  - mean
  - median
  - variance
  - probability
  - correlation
  - statistics

- Generated embedding vectors for these words.
- Obtained an embedding matrix with shape `(6, 300)`.

### 9. Saving GloVe Embeddings

Saved the generated GloVe embeddings as:

`statistics_glove_embeddings.npy`

## 📊 Results

| Experiment | Output |
|---|---|
| PDF Extraction | 54 pages processed |
| Sentence Tokenization | 1003 sentences |
| Word2Vec Vector Size | 100 |
| Word2Vec Similar Words | Top 5 words for `mean` |
| GloVe Words | 6 statistical terms |
| GloVe Embedding Shape | (6, 300) |

## 🔍 Word2Vec vs GloVe

| Word2Vec | GloVe |
|---|---|
| Trained on the extracted PDF text | Uses pre-trained word embeddings |
| Learns word representations from the given corpus | Uses embeddings learned from a larger text corpus |
| Generated 100-dimensional vectors | Generated 300-dimensional vectors |
| Implemented using Gensim | Loaded using StaticVectors |

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Static-Word-Embeddings-from-PDF.git
```

Navigate to the project folder:

```bash
cd Static-Word-Embeddings-from-PDF
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

Alternatively, open and execute the notebook:

```bash
jupyter notebook Statistics_Word_Embeddings.ipynb
```

**Note:** Keep the input PDF in the project folder before running the script. GloVe model loading may require an internet connection.

## 📄 Requirements

The project uses the following Python libraries:

```text
numpy
pypdf
gensim
staticvectors
jupyter
notebook
```

## ⚠️ Limitations

- The Word2Vec model is trained on a single PDF document, so its vocabulary and semantic relationships are limited by the available text.
- Similar-word results may not always represent meaningful semantic relationships.
- PDF text extraction can introduce formatting or character-recognition issues.
- GloVe embeddings depend on the vocabulary available in the pre-trained model.

## 🚀 Future Enhancements

- Improve PDF text cleaning and preprocessing.
- Compare Word2Vec and GloVe embeddings in more detail.
- Visualize word embeddings using dimensionality reduction techniques such as PCA or t-SNE.
- Evaluate word similarity using a larger statistical vocabulary.
- Experiment with different Word2Vec parameters.



## 📝 Conclusion

This project demonstrates the practical implementation of static word embeddings using Word2Vec and GloVe.

It covers the complete workflow, starting from PDF text extraction and preprocessing to generating, analyzing, and saving word embeddings.

The project provides hands-on experience with NLP preprocessing techniques and static word representation methods.
