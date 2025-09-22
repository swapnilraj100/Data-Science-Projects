# 🧠 Semantic Analytics on CodeMix Using NLP

This project addresses the challenge of **sentiment analysis for Tamil-English code-mixed text**, commonly found in social media.  
It builds an **end-to-end semantic analytics pipeline** and evaluates models ranging from classical ML to advanced hybrid deep learning architectures.

---

## 📌 Project Overview
- **Domain**: Natural Language Processing (NLP), Sentiment Analysis.
- **Dataset**: `tamil_sentiment_full.csv` – Tamil-English code-mixed text with sentiment labels.
- **Objective**: Accurately classify sentiments (positive, negative, neutral) in noisy, morphologically-rich, code-switched text.

---

## 📂 Repository Structure
- **Datasets Used/**
  - `tamil_sentiment_full.csv` → Tamil-English code-mixed sentiment dataset.

- **Models Trained/**
  - `BERT_Transformer Models.ipynb` → Transformer-based sentiment classification.
  - `FastText_BiLSTM_CharCNN_Hybrid_Model.ipynb` → Combines FastText embeddings, BiLSTM, and CharCNN.
  - `Transformer_BiGRU_CNN _Hybrid_Model.ipynb` → Hybrid model with Transformer encoders, BiGRU, and CNN layers.

- **Reports/**
  - `Best Transformer Hybrid Model Report.pdf` → Detailed evaluation of the best hybrid model.
  - `SACM_NLP_Reserach_PaperWork.pdf` → Full research methodology and results.

---

## ⚙️ Techniques Explored
- **Classical ML**: TF-IDF + SVM, Logistic Regression.
- **Deep Learning**:
  - BiLSTM, CNN-BiLSTM, Attention-based RNNs.
  - FastText embeddings with hybrid layers.
- **Transformers**: BERT,
  - mBERT
  - XLM-RoBERTa
  - IndicBERT
  - MURIL
- **Hybrid Architectures**:
  - CharCNN + BiLSTM + Attention.
  - **MuRIL-BERT + CharCNN + CNN-BiGRU + Attention + Statistical Features** (Best Model).

---

## 🏆 Best Model: Hybrid MuRIL-BERT Fusion
### Architecture:
- **MuRIL-BERT embeddings** for multilingual representation.
- **CharCNN** for character-level noise robustness.
- **Word-level CNN (multi-kernel)** for n-gram features.
- **BiGRU with Attention** for contextual sequence learning.
- **Statistical feature fusion** (TF-IDF, sentiment lexicons).
  
### Performance:
- Achieved **highest F1-score and accuracy** on Tamil-English dataset.
- Outperformed standalone BERT, BiLSTM, CNN, and FastText-based hybrids.
- Especially strong on **noisy social media text**.

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone <repo_url>
   cd "Semantic Analytics on CodeMix Using NLP"
Install dependencies:

bash
Copy code
pip install -r requirements.txt
(include TensorFlow / PyTorch, HuggingFace Transformers, FastText, etc.)

Run Jupyter notebooks in Models Trained/ to reproduce experiments.

📊 Key Findings
Classical ML (SVM, Logistic Regression) provides baselines but underperforms.

BiLSTM and CNN-based hybrids improve performance but still struggle with noisy tokens.

Hybrid MuRIL-BERT with CharCNN + CNN-BiGRU + Attention + Statistical Features delivers state-of-the-art results for Tamil-English code-mixed sentiment analysis.

📌 Future Work
Deploy models as an API using FastAPI + Docker.

Integrate MLflow for experiment tracking.

👨‍💻 Author
Swapnil Raj (M.Tech Research, NIT Jamshedpur)

Under the guidance of Dr. Jitesh Pradhan

Department of Computer Science & Engineering, NIT Jamshedpur