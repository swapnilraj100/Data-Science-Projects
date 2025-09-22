# 🚀 Build, Train & Deploy Machine Learning Models

This repository is a **complete end-to-end machine learning & deep learning project hub**, covering:
- **Classical ML with Python**
- **Deep Learning with ANN, CNN, RNN**
- **EDA & Feature Engineering**
- **Deployment pipelines with Docker & GitHub Actions**

---

## 📌 Repository Structure

### 1. Machine Learning With Python
- **ClassificationModels_ML.ipynb** → Logistic Regression, Decision Trees, Random Forests, etc.
- **RegressionModels_ML.ipynb** → Linear Regression, Polynomial Regression, etc.
- **Feature Engineering** → EDA on GDP, Google Play Store, Outliers.
- **Data Analysis Project** → Sensor dataset analysis with problem statement.
- **Python Libraries** → Tutorials on Numpy, Pandas, Matplotlib.

### 2. Deep Learning Models
- **ANN Models** → California Housing, Iris, MNIST (with hyperparameter tuning).
- **CNN Models** → CIFAR-10, CIFAR-100, Fashion-MNIST, MNIST Digits, plus a medical AI project (**Glaucoma Detection**).
- **RNN Models** → LSTM and BiLSTM variations for sequential data.
- **Datasets** → Stock prices, Tamil sentiment dataset, etc.

### 3. Machine Learning Deployment Pipeline
- **app.py** → Flask/FastAPI app exposing trained model as API.
- **Dockerfile** → Containerization setup for deployment.
- **requirements.txt** → Python dependencies.
- **GitHub Actions** → CI/CD workflow for automated Docker image builds.
- **models/** → Pretrained ML pipelines (`.joblib` files).

---

## ⚙️ Tech Stack
- **Python**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- **Deep Learning**: TensorFlow / Keras
- **Deployment**: Flask / FastAPI, Docker, GitHub Actions
- **ML Ops**: Model serialization (`joblib`), CI/CD with workflows

---

## 📊 Key Use Cases
- Customer/product segmentation (unsupervised learning).
- Classification tasks (e.g., Iris, Diabetes dataset).
- Regression tasks (e.g., California Housing, Stock price prediction).
- Computer Vision tasks (CIFAR, Fashion-MNIST, Medical Imaging).
- NLP tasks (Tamil sentiment analysis).
- Deployment-ready ML services.

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone <repo_url>
   cd Build-Train-Deploy-Machine Learning Models
   ```
2. Install dependencies:
   ```bash
   pip install -r Machine\ Learning\ Deployment\ Pipeline/requirements.txt
   ```
3. Run Jupyter notebooks for training and experiments.
4. For deployment:
   ```bash
   cd Machine\ Learning\ Deployment\ Pipeline
   docker build -t ml-model .
   docker run -p 5000:5000 ml-model
   ```

---

## 📌 Future Improvements
- Integrate **KServe** or **BentoML** for scalable model serving.
- Add **MLflow** for experiment tracking.
- Extend to **transformer-based NLP models**.

---

## 👨‍💻 Author
This project is a consolidated portfolio of **machine learning, deep learning, and MLOps** workflows.
