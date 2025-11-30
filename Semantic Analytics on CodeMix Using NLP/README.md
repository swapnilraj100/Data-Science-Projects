# SACMT: South-Indian ASR Hybrid Models

This repository contains Jupyter notebooks for training and evaluating hybrid Automatic Speech Recognition (ASR) models for three South-Indian languages:

- Kannada: `Kannada_Hybrid_Model.ipynb`
- Malayalam: `Malyalam_Hybrid_Model.ipynb`
- Tamil: `Tamil_Hybrid_Model.ipynb`

Each notebook encapsulates data preparation, acoustic/lexical modeling, and evaluation steps for a hybrid (e.g., HMM + DNN) pipeline tailored to the respective language.

## Features
- End-to-end, language-specific ASR workflows in notebooks.
- Modular cells for data preprocessing, feature extraction, model training, and decoding.
- Windows-friendly commands and instructions using PowerShell.

## Prerequisites
- OS: Windows 10/11 (PowerShell 5.1)
- Python 3.9+ recommended
- Jupyter Notebook or VS Code with the Jupyter extension
- GPU (optional) for faster training

## Quick Start

1. Create and activate a virtual environment (recommended):

```powershell
# From the repository root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

2. Install core dependencies:

```powershell
# If a requirements file exists, prefer that
if (Test-Path -Path "requirements.txt") { pip install -r requirements.txt } else { 
    pip install jupyter numpy scipy pandas scikit-learn matplotlib librosa torch torchaudio
}
```

3. Launch Jupyter and open a notebook:

```powershell
jupyter notebook
```

Open one of:
- `Kannada_Hybrid_Model.ipynb`
- `Malyalam_Hybrid_Model.ipynb`
- `Tamil_Hybrid_Model.ipynb`

Execute cells sequentially. Adjust paths and hyperparameters as needed.

## Notebook Structure (Typical)
- Data setup: Paths, dataset checks, train/val/test split.
- Preprocessing: Audio resampling, trimming, normalization, feature extraction (MFCC/FBANK).
- Lexicon/Language model: Grapheme-to-phoneme (G2P) or direct lexicon loading; optional n-gram LM.
- Acoustic model: Hybrid HMM-DNN (e.g., GMM init, then DNN).
- Decoding & Evaluation: Beam search parameters, WER/CER metrics, confusion analysis.

## Data
- Place raw audio and transcripts in a language-specific folder (e.g., `data/kannada`, `data/malayalam`, `data/tamil`).
- Expected structure (example):
  - `data/<lang>/audio/*.wav`
  - `data/<lang>/train.tsv`, `dev.tsv`, `test.tsv` (or CSV), with columns: `path`, `text`.
- Update paths in the first cells of each notebook.

## Configuration
- Key parameters are defined at the top of each notebook:
  - Sampling rate, feature type and dimensions
  - Model architecture and training schedule
  - Decoding beam width and LM weights

## Tips for Windows/PowerShell
- Use backslashes in paths or double-quoted strings, e.g., `"f:\\data\\kannada"`.
- If you encounter permission issues, run PowerShell as Administrator.
- For long paths, enable long path support in Windows if needed.

## Reproducibility
- Set random seeds in notebooks for `numpy`, `torch`, and any other libraries.
- Pin dependency versions via `requirements.txt` for consistent results.
- Document dataset versions and preprocessing steps.

## Troubleshooting
- Package installation errors: ensure `.venv` is active and `pip` is updated.
- CUDA/GPU issues: install a PyTorch build matching your CUDA version, or fall back to CPU.
- Audio loading errors: confirm WAV format compatibility and sampling rates.

## Roadmap
- Add `requirements.txt` with pinned versions per language.
- Export trained models and decoding scripts for CLI usage.
- Add data download helpers and automated evaluation reports.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Citation
If you use these notebooks, please cite appropriately. Add a BibTeX entry here when available.
