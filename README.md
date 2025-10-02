# Resume Analyzer

> Intelligent resume parsing & scoring web app — built with Python & Streamlit.

---

## 🔍 What it does

Resume Analyzer extracts key details from resumes, compares them against job descriptions, and provides improvement suggestions. It uses Streamlit for a simple and interactive UI.

## 🚀 Highlights

* Upload resumes in PDF/DOCX format
* Extract name, contact, education, skills, and experience
* Match resumes with job descriptions
* Generate a relevance score
* Provide actionable suggestions to improve resume alignment
* Lightweight and modular for future enhancements

## 🧭 Tech stack

* **Framework/UI:** Python (Streamlit)
* **Parsing & NLP:** PyPDF2, docx2txt, NLTK/spaCy
* **Visualization:** Plotly (for score insights)
* **Helper scripts:** Python utilities for scoring and parsing

## 🛠️ Quick start

```bash
# 1. clone the repo
git clone https://github.com/bargavjillella/resume-analyzer.git
cd resume-analyzer

# 2. create a python virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. install dependencies
pip install -r requirements.txt

# 4. run the app with Streamlit
streamlit run app.py
```

> Once running, open the link shown in your terminal (usually [http://localhost:8501/](http://localhost:8501/)).

## 📂 Project Structure

```
resume-analyzer/
├─ .venv/              # Virtual environment (not tracked)
├─ venv/               # Alternate virtual environment (not tracked)
├─ data/               # Sample resumes, job descriptions, and data files
├─ utils/              # Utility functions (helpers for parsing/scoring)
│
├─ app.py              # Main Streamlit entry point
├─ run.py              # Script to run backend logic
├─ index.html          # Landing page / static template
├─ style.css           # Styles for UI components
├─ app.js              # Frontend JavaScript logic
├─ app_1.js            # Additional frontend JS (optional/experimental)
├─ requirements.txt    # Python dependencies
├─ .gitattributes      # Git configuration
└─ README.md           # Project documentation
```

## ✅ How to use (user flow)

1. Run the app with Streamlit.
2. Upload a resume file (PDF/DOCX).
3. Paste or upload a job description.
4. View extracted resume details.
5. Check the match score and improvement suggestions.

## ♻️ Extending the project

* Add ML-based scoring instead of keyword matching.
* Deploy on Streamlit Cloud, Heroku, or AWS.
* Batch processing for multiple resumes.
* REST API for external integrations.

## 📝 Contribution guidelines

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit with clear messages.
4. Open a Pull Request for review.


*Streamlit-powered, simple to use, and easy to extend.*
