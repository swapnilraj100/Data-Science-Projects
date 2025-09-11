# Semantic Analysis on Code-Mixed Text Languages

This repository contains the implementation and research work for my **M.Tech thesis project** at **NIT Jamshedpur** on **Semantic Analytics of Tamil-English Code-Mixed Text**.  
The work compares **classical ML baselines, deep learning architectures (BiLSTM + CNN), and state-of-the-art multilingual transformers (mBERT, IndicBERT, MuRIL, XLM-RoBERTa)**.

## 📑 Research Paper
The full research details are documented in the paper:  
- [Semantic Analysis on Code-Mixed Text Languages (PDF)](SACM_NLP_Reserach_PaperWork.pdf)

## 📂 Repository Structure
```
├── BiLSTM__Variations.ipynb         # BiLSTM, Stacked, Dropout, CNN-BiLSTM, Attention-BiLSTM
├── Fine_Tuned_MuRIL.ipynb           # Transformer-based fine-tuning (MuRIL)
├── BERT_Variations.ipynb     # mBERT, IndicBERT, MuRIL,XLM-RoBERTa comparisons
├── SACM_NLP_Reserach_PaperWork.pdf  # Research paper with methodology & results
└── README.md                        # Project documentation
```

## 🧪 Models Implemented
### Classical ML Baselines
- TF-IDF + SVM  
- TF-IDF + Logistic Regression  

### Deep Learning
- BiLSTM  
- BiLSTM with Dropout  
- Stacked BiLSTM  
- CNN + BiLSTM  
- Attention BiLSTM  

### Transformer Models
- **mBERT**  
- **IndicBERT**  
- **MuRIL** (fine-tuned, best performing)  
- **XLM-RoBERTa**

## 📊 Results
- **Classical models**: Weighted F1 ≈ 0.41  
- **BiLSTM variations**: struggled with class imbalance (F1 ≈ 0.02–0.41)  
- **Transformers**: Strong performance, with **MuRIL** emerging as the top model (Weighted F1 = **0.60**, Macro F1 = **0.52**).  

## ⚙️ Tech Stack
- Python 3.x  
- TensorFlow / Keras  
- PyTorch (for transformers via HuggingFace)  
- Scikit-learn  
- Flask, Docker, Kubernetes (for deployment pipeline)

## 🚀 How to Run
1. Clone this repo  
   ```bash
   git clone https://github.com/<your-username>/Semantic-Analysis-Codemix.git
   cd Semantic-Analysis-Codemix
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Open notebooks  
   ```bash
   jupyter notebook
   ```
4. Run experiments for BiLSTM and transformer models.

## 📝 Citation
If you use this work, please cite:  

```
Swapnil Raj, "Semantic Analysis on Code-Mixed Text Languages," 
M.Tech Thesis Project, NIT Jamshedpur, 2024.
```

## 👨‍💻 Author
**Swapnil Raj**  
- M.Tech, Data Science | NIT Jamshedpur  
- Former Solution Integrator, Ericsson  
- 📧 swapnilraj100@gmail.com  
